from sqlalchemy import create_engine, Column, String, Text, Integer, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('{連線位置}',
                       encoding = 'utf-8',
                       echo = True)
Base = declarative_base()
Session = sessionmaker(bind = engine)

class Tests(Base):
    __tablename__ = "Tests"

    id = Column(Integer, primary_key = True)
    name = Column(Text)

if __name__ == '__main__':
    Base.metadata.create_all(engine)