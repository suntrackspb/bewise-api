import os

from dotenv import load_dotenv

if os.getenv("MODE") == "TEST":
    load_dotenv(".env.test")
elif os.getenv("MODE") == "PROD":
    load_dotenv(".env")
else:
    load_dotenv(".env.local")

DB_NAME: str = os.getenv("DB_NAME", default="postgres")
DB_USER: str = os.getenv("DB_USER", default="postgres")
DB_PASS: str = os.getenv("DB_PASS", default="postgres")
DB_HOST: str = os.getenv("DB_HOST", default="localhost")
DB_PORT: str = os.getenv("DB_PORT", default="5432")

POSTGRES_URL: str = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
