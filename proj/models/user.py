from sqlalchemy import Column, Integer, String, LargeBinary
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User(Base):
    """User Class
    Args:
        user_name: 
        email:
        password:
    """
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    email = Column(String(60), nullable=False, unique=True)
    password = Column(String(60), nullable=False)
    gender = Column(String(7))
    level = Column(String(60))
    job = Column(String(60))
    country = Column(String(60))
    age = Column(Integer, nullable=False)
    weight = Column(Integer)
    height = Column(Integer)
    situation = Column(String(20))
    diseases = Column(String(60))
    img = Column(String(60))
    
    
    def __str__(self):
        return self.email
    
 