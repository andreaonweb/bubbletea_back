import os
import pymysql
from dotenv import load_dotenv

load_dotenv()

def get_db_connection():
    try:
        conn = pymysql.connect(
            host=os.getenv("DB_HOST"),
            port=int(os.getenv("DB_PORT")),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME"),
            ssl={"ssl": {}},
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor
        )
        print("✅ Conectado a Aiven")
        return conn
    except Exception as e:
        print(f"❌ Error conectando a la DB: {e}")
        return None