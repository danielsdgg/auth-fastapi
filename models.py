from sqlalchemy import create_engine, String, Column, Integer
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Admin(Base):
    __tablename__ = 'admin'
    id = Column(Integer(), primary_key = True)
    username = Column(String())
    full_name = Column(String())
    email = Column(String())
    hashed_password = Column(String())
    disabled = False

    def __repr__(self):
        return f'<admin: {self.username}>'

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer(), primary_key = True)
    name = Column(String())
    password = Column(String())

    def __repr__(self):
        return f'<users: {self.name}>'

engine = create_engine('sqlite:///dan.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind = engine)
session = Session()
