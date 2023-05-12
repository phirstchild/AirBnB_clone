#!/usr/bin/python3

"""
This  module will implements the BaseModel class
"""

from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    This is the head class for  attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the BaseModel class
        """

        from models import storage
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.now()
            storage.new(self)
        else:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ('created_at', 'updated_at'):
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)

    def __str__(self):
        """
        Returns the BaseModel object representation as a string.
        [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(type(self).__name__, self.id,
                                     self.__dict__)

    def save(self):
        """
        Updates 'self.updated_at' with the current datetime
        """
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__
        of the instance:

        - only instance attributes set will be returned
        - a key __class__ is added with the class name of the object
        - created_at and updated_at must be converted to string object in ISO
        object
        """
        dict_all = self.__dict__.copy()
        dict_all["__class__"] = self.__class__.__name__
        for k, v in self.__dict__.items():
            if k in ("created_at", "updated_at"):
                v = self.__dict__[k].isoformat()
                dict_all[k] = v
        return dict_all
