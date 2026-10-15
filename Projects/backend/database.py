from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL= "mysql+pymysql://root:siva@localhost:3306/project"

engine=create_engine(DATABASE_URL)
SessionLocal=sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base=declarative_base() #Base is used to create your database model

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
        