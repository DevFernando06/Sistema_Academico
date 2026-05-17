import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

def create_connection():
    try:
        conn = psycopg2.connect(
            dbname=os.environ.get('DB_NAME'),
            user=os.environ.get('DB_USER'),
            password=os.environ.get('DB_PASS'),
            host='localhost',
            port='5432'
        )
        return conn

    except Exception as e:
        print(e)
