import uuid
from sqlalchemy.sql import func
from models.model import Base, Model, relationship
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from flask_login import UserMixin

class User(Base, Model, UserMixin):
    """ 
        User represents the members of all groups
    """
    __tablename__ = 'users'

    id = Column(String(60), primary_key=True, default=str(uuid.uuid4()), nullable=False)
    name = Column(String(254), nullable=False)
    email = Column(String(254), nullable=False, unique=True)
    password = Column(String(254), nullable=False)
    date_online = Column(DateTime, default=func.now())
    posts = relationship("Post", back_populates="author", lazy=True)
