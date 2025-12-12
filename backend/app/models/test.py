from sqlalchemy import Column, Integer
from sqlalchemy.types import Text
from app.core.database import Base


class Test(Base):
    __tablename__ = "test"
    
    id = Column(Integer, primary_key=True, index=True)
    test = Column(Text)

