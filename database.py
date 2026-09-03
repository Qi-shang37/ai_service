import os
import mysql.connector

db_config = {
    "host": "localhost",
    "user": "root",
    "password": os.environ.get("DB_PASSWORD", ""),
    "database": "ai_service"
}

def log_inference(input_text, sentiment, confidence):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    sql = "INSERT INTO inference_logs (input_text, sentiment, confidence) VALUES (%s, %s, %s)"
    cursor.execute(sql, (input_text, sentiment, confidence))
    conn.commit()
    cursor.close()
    conn.close()
