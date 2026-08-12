import os
import django
from django.conf import settings
from pathlib import Path

# Setup minimal django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'coworkconnect.settings')
django.setup()

from django.db import connection

def run():
    with connection.cursor() as cursor:
        try:
            cursor.execute("ALTER TABLE users ADD COLUMN avatar_url TEXT;")
            print("Added avatar_url column")
        except Exception as e:
            print("Error adding avatar_url:", e)
        
        try:
            cursor.execute("ALTER TABLE users ADD COLUMN expertise TEXT;")
            print("Added expertise column")
        except Exception as e:
            print("Error adding expertise:", e)

        try:
            cursor.execute("ALTER TABLE spaces ADD COLUMN images TEXT;")
            print("Added spaces.images column")
        except Exception as e:
            print("Error adding spaces.images:", e)

        try:
            cursor.execute("ALTER TABLE spaces ADD COLUMN rating REAL DEFAULT 4.9;")
            print("Added spaces.rating column")
        except Exception as e:
            print("Error adding spaces.rating:", e)

        try:
            cursor.execute("ALTER TABLE spaces ADD COLUMN user_id INT;")
            print("Added spaces.user_id column")
        except Exception as e:
            print("Error adding spaces.user_id:", e)

        try:
            cursor.execute("ALTER TABLE spaces ADD COLUMN contact_email TEXT;")
            print("Added spaces.contact_email column")
        except Exception as e:
            print("Error adding spaces.contact_email:", e)

        try:
            cursor.execute("ALTER TABLE spaces ADD COLUMN contact_phone TEXT;")
            print("Added spaces.contact_phone column")
        except Exception as e:
            print("Error adding spaces.contact_phone:", e)

        try:
            cursor.execute("ALTER TABLE spaces ADD COLUMN website_url TEXT;")
            print("Added spaces.website_url column")
        except Exception as e:
            print("Error adding spaces.website_url:", e)

if __name__ == '__main__':
    run()
