from sqlmodel import create_engine, Session
from typing import Generator
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv(
    "DATABASE_URL"
)  # e.g. postgresql://user:pass@localhost/db_name

engine = create_engine(DATABASE_URL, echo=True)


def get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session
