from db.database import Base
from sqlalchemy import Column, Integer, Date, String, Boolean, text, TIMESTAMP

class User(Base):
    __tablename__ = "usuarios"

    id = Column(Integer,primary_key=True,nullable=False,autoincrement=True)
    name = Column(String,nullable=False)
    surname = Column(String,nullable=False)
    email = Column(String,nullable=False)
    password = Column(String,nullable=False)
    fchnace = Column(Date,nullable=False)
    
#    start_time = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('Now()'))
#    end_time = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('Now()'))
    
