from sqlalchemy import Column, Integer
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Metrics(Base):
    __tablename__ = "metrics"

    user_id = Column(Integer, primary_key=True)
    value = Column(Integer)
