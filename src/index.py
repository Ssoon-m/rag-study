from dotenv import load_dotenv
import os

def main():
    load_dotenv()

    db_id       = os.getenv("DATABASE_ID")
    db_password = os.getenv("DATABASE_PASSWORD")

    print(f"DATABASE_ID={db_id}")
    print(f"DATABASE_PASSWORD={db_password}")

if __name__ == "__main__":
    main()
