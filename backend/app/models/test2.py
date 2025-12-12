from sqlalchemy import Column, Integer
from sqlalchemy.types import Text
from app.core.database import Base


class Test2(Base):
    __tablename__ = "test2"
    
    id = Column(Integer, primary_key=True, index=True)
    test = Column(Text)

