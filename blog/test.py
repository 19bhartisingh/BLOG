from sqlalchemy.orm import Session
from database import SessionLocal  
from sqlalchemy import text

def test_connection():
    try:
        db: Session = SessionLocal()
        result = db.execute(text('SELECT 1')).scalar()
        if result == 1:
            print("✅ Connection to SQL Server is successful!")
        else:
            print("⚠️ Connected, but unexpected response.")
    except Exception as e:
        print("❌ Failed to connect to SQL Server.")
        print("Error:", e)
    finally:
        db.close()

if __name__ == "__main__":
    test_connection()
