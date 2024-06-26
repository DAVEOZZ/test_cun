import psycopg2
from psycopg2.extras import RealDictCursor
import os

DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_MOTOR=os.getenv('DB_MOTOR')
#DATABASE_URL = DB_MOTOR+"://"+DB_USER+":"+DB_PASSWORD+"@"+DB_HOST+"/"+DB_NAME
DATABASE_URL = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'

def get_db_connection():
    conn = psycopg2.connect(DATABASE_URL, cursor_factory=RealDictCursor) # easiness to get a query output as json.
    return conn
