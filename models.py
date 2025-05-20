from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()
engine = create_engine(
    "sqlite:///moltress.db"
)


class RulesRead(Base):
    __tablename__ = "rules_read"

    username = Column(String, primary_key=True)
    date = Column(String)


Base.metadata.create_all(engine)

