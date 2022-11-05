""" base Model for all models """

from uuid import uuid4
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.sql import func
from sqlalchemy import Column, DateTime
import models

Base = declarative_base()
relationship = relationship

time = "%Y-%m-%dT%H:%M:%S.%f"


class Model:
    """
        basemodel for all other models
    """

    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(DateTime, default=func.now(), nullable=False)


    @classmethod
    def all(self):
        """
            save requested data to database
        """

        allObjs = models.session.query(self).all()
        return allObjs

    @classmethod
    def where(self, **kwargs):
        data = models.session.query(self).filter_by(**kwargs).one_or_none()
        return data


    @classmethod
    def get(self, id):
        """
            save requested data to database
        """
        data = models.session.query(self).filter(self.id == id).first()
        return data

    def save(self):
        """
            save requested data to database
        """
        self.id = uuid4()
        models.session.add(self)
        models.session.commit()
        return True


    def update(self, **kwargs):
        """
            update data
        """
        for k, v in kwargs.items():
                setattr(self, k, v)
        
        data = models.session.commit()
        return data
        # models.session.query(self).update

    def to_dict(self):
        """ 
        covert objet to dict
        """     
        new_dict = self.__dict__.copy()

        if "created_at" in new_dict:
            new_dict['created_at'] = new_dict['created_at'].strftime(time)
        
        if "updated_at" in new_dict:
            new_dict['updated_ta'] = new_dict['updated_at'].strftime(time)
        
        if "_sa_instance_state" in new_dict:
            del new_dict['_sa_instance_state']
        return new_dict