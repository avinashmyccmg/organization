from sqlalchemy import Column, Integer, String
from database import Base


class Organization(Base):
  __tablename__ = "organizations"

  id = Column(Integer, primary_key=True, index=True)
  name = Column(String)
