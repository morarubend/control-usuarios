from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#SQLALCHEMY_DATABASE_URL = ('postgresql://rdmq:rdmq@localhost:5433/rdmq', echo=True)
#engine = create_engine('postgresql://rdmq:rdmq@localhost:5433/clientes', echo=True)
engine = create_engine('postgresql://rdmq:rdmq@db/clientes')

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        