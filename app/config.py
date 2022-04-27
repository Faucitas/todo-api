from dotenv import load_dotenv
import os

load_dotenv()

DB_USER = os.getenv('DB_USERNAME')
DB_SERVER = os.getenv('DB_SERVER')
DB_NAME = os.getenv('DB_NAME')
DB_PASSWORD = os.getenv('DB_PASSWORD')

SQLALCHEMY_DATABASE_URI = f"postgresql://{DB_USER}@{DB_SERVER}/{DB_NAME}"
SQLALCHEMY_TRACK_MODIFICATIONS = False
