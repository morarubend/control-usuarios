from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#SQLALCHEMY_DATABASE_URL = ('postgresql://rdmq:rdmq@localhost:5433/rdmq', echo=True)
#engine = create_engine('postgresql://rdmq:rdmq@localhost:5433/clientes', echo=True)
#engine = create_engine('postgresql://rdmq:rdmq@db/clientes')
engine = create_engine('postgresql://morabase_user:Ti4f7376sSV3ez4q9y56iqI8S4u8YoOI@dpg-cq85qsss1f4s73cfuc70-a/morabase')

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        