import uuid 
from sqlalchemy import Column, Integer, String, JSON, ForeignKey
from models.model import Model, Base, relationship
class Post(Base, Model):
    """ post model class """
    __tablename__ = 'posts'
    id = Column(String(60), primary_key=True, default=str(uuid.uuid4()), nullable=False)
    title = Column(String(100), nullable=False)
    content = Column(JSON, nullable=False)
    author_id = Column(String(60), ForeignKey("users.id"))
    author = relationship("User", back_populates="posts")
