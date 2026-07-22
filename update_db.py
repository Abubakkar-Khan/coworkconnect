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

if __name__ == '__main__':
    run()
