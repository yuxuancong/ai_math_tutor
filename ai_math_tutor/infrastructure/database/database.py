import psycopg2
from psycopg2.extras import DictCursor
from typing import Dict, Any, List
from ..config.settings import Settings

class DatabaseManager:
    def __init__(self):
        self.conn_params = {
            'host': Settings.DB_HOST,
            'port': Settings.DB_PORT,
            'database': Settings.DB_NAME,
            'user': Settings.DB_USER,
            'password': Settings.DB_PASSWORD
        }
        
    def get_connection(self):
        return psycopg2.connect(**self.conn_params)
        
    def save_progress(self, student_id: str, concept: str, progress: Dict[str, Any]) -> bool:
        """Save student learning progress"""
        query = """
            INSERT INTO learning_progress (student_id, concept, mastery_level, timestamp)
            VALUES (%s, %s, %s, NOW())
            ON CONFLICT (student_id, concept) 
            DO UPDATE SET mastery_level = %s, timestamp = NOW()
        """
        try:
            with self.get_connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(query, (
                        student_id,
                        concept,
                        progress['mastery_level'],
                        progress['mastery_level']
                    ))
                    return True
        except Exception as e:
            logger.error(f"Database error: {str(e)}")
            return False 