from datetime import date
from typing import Optional

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase


engine = create_engine(
    "sqlite:///moltress.db"
)

class Base(DeclarativeBase):
    pass

class RulesRead(DeclarativeBase):
    __tablename__ = "rules_read"

    id: Mapped[str] = mapped_column(primary_key=True)
    date: Mapped[Optional[date]]

DeclarativeBase.metadata.tables['rules_read']


def get_session():
    Session = sessionmaker(bind=engine)
    return Session()

