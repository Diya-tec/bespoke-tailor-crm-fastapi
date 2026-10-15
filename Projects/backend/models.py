from sqlalchemy import Column,Integer,String,BigInteger
from database import Base

class User(Base):
    __tablename__="clothes"
    id=Column(Integer,primary_key=True)
    name=Column(String(100),nullable=False)
    phno=Column(BigInteger,unique=True,nullable=False)
    shirt_shoulder=Column(Integer,nullable=True)
    shirt_length=Column(Integer,nullable=True)
    shirt_hand=Column(String(25),nullable=True)
    pants_length=Column(Integer,nullable=True)
    pants_style=Column(String(100),nullable=True)
    pants_waist=Column(Integer,nullable=True)