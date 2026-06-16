from pathlib import Path
import os
import tempfile
from urllib.parse import parse_qs, urlparse, unquote


BASE_DIR = Path(__file__).resolve().parent.parent


def load_env():
    if truthy(os.getenv("VERCEL", "false")):
        return

    env_path = BASE_DIR / ".env"
    if not env_path.exists():
        return

    for line in env_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


def truthy(value):
    return str(value).lower() in {"1", "true", "yes", "on", "require", "required"}


load_env()

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", os.getenv("JWT_SECRET", "coworkconnect-dev-key"))
DEBUG = os.getenv("DEBUG", "true").lower() == "true"
ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    "django.contrib.staticfiles",
    "api.apps.ApiConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.middleware.common.CommonMiddleware",
    "api.middleware.EnsureSchemaMiddleware",
    "api.middleware.CorsMiddleware",
]

ROOT_URLCONF = "coworkconnect.urls"
WSGI_APPLICATION = "coworkconnect.wsgi.application"
ASGI_APPLICATION = "coworkconnect.asgi.application"


def database_config_from_env():
    database_url = (
        os.getenv("DATABASE_URL")
        or os.getenv("POSTGRES_URL")
        or os.getenv("SUPABASE_DATABASE_URL")
        or os.getenv("MYSQL_URL")
    )
    config = {
        "engine": os.getenv("DB_ENGINE", "mysql"),
        "name": os.getenv("DB_NAME", "coworkconnect"),
        "host": os.getenv("DB_HOST", "localhost"),
        "user": os.getenv("DB_USER", "root"),
        "password": os.getenv("DB_PASSWORD", ""),
        "port": os.getenv("DB_PORT", "3306"),
        "ssl": truthy(os.getenv("DB_SSL", "false")),
    }

    if database_url:
        parsed = urlparse(database_url)
        query = parse_qs(parsed.query)
        scheme = parsed.scheme.replace("+psycopg", "")
        engine = "postgresql" if scheme in {"postgres", "postgresql"} else "mysql"
        config.update(
            {
                "engine": engine,
                "name": parsed.path.lstrip("/") or config["name"],
                "host": parsed.hostname or config["host"],
                "user": unquote(parsed.username or config["user"]),
                "password": unquote(parsed.password or config["password"]),
                "port": str(parsed.port or ("5432" if engine == "postgresql" else config["port"])),
                "ssl": config["ssl"]
                or "ssl" in query
                or truthy(query.get("ssl-mode", [""])[0])
                or truthy(query.get("sslmode", [""])[0]),
            }
        )

    return config


USE_SQLITE_FALLBACK = (
    truthy(os.getenv("VERCEL", "false"))
    and not os.getenv("DATABASE_URL")
    and not os.getenv("POSTGRES_URL")
    and not os.getenv("SUPABASE_DATABASE_URL")
    and not os.getenv("MYSQL_URL")
    and not os.getenv("DB_HOST")
)

DB_CONFIG = database_config_from_env()
DB_ENGINE = DB_CONFIG["engine"]
DB_NAME = DB_CONFIG["name"]
DB_HOST = DB_CONFIG["host"]
DB_USER = DB_CONFIG["user"]
DB_PASSWORD = DB_CONFIG["password"]
DB_PORT = DB_CONFIG["port"]
DB_SSL = DB_CONFIG["ssl"]

if not USE_SQLITE_FALLBACK and DB_ENGINE == "mysql":
    try:
        import pymysql

        connection = pymysql.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            port=int(DB_PORT),
            charset="utf8mb4",
            autocommit=True,
            ssl={} if DB_SSL else None,
        )
        with connection.cursor() as cursor:
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS `{DB_NAME}` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
        connection.close()
    except Exception:
        pass

if USE_SQLITE_FALLBACK:
    SQLITE_PATH = Path(os.getenv("SQLITE_PATH", Path(tempfile.gettempdir()) / "coworkconnect.sqlite3"))
    SQLITE_PATH.parent.mkdir(parents=True, exist_ok=True)
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": str(SQLITE_PATH),
        }
    }
else:
    django_engine = "django.db.backends.postgresql" if DB_ENGINE == "postgresql" else "django.db.backends.mysql"
    db_options = {}
    if DB_ENGINE == "mysql":
        db_options = {
            "charset": "utf8mb4",
            **({"ssl": {}} if DB_SSL else {}),
        }
    elif DB_ENGINE == "postgresql" and DB_SSL:
        db_options = {"sslmode": "require"}

    DATABASES = {
        "default": {
            "ENGINE": django_engine,
            "NAME": DB_NAME,
            "USER": DB_USER,
            "PASSWORD": DB_PASSWORD,
            "HOST": DB_HOST,
            "PORT": DB_PORT,
            "OPTIONS": db_options,
        }
    }

LANGUAGE_CODE = "en-us"
TIME_ZONE = "Asia/Karachi"
USE_I18N = True
USE_TZ = False

STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "ui"]
MEDIA_URL = "/uploads/"
MEDIA_ROOT = Path(tempfile.gettempdir()) / "uploads" if USE_SQLITE_FALLBACK else BASE_DIR / "uploads"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

JWT_SECRET = os.getenv("JWT_SECRET", SECRET_KEY)
JWT_EXPIRE = os.getenv("JWT_EXPIRE", "30d")
