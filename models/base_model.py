#!/usr/bin/python3
""" This is a class which defines all common attributes/methods for
    other classes
"""
from datetime import datetime
import uuid


class BaseModel():

    """ This serves as a base model for other classes in this package """
    def __init__(self, *args, **kwargs):
        """ initialize instance attributes"""
        if kwargs and len(kwargs) != 0:
            if '__class__' in kwargs:
                del kwargs['__class__']
            kwargs['created_at'] = datetime.fromisoformat(kwargs['created_at'])
            kwargs['updated_at'] = datetime.fromisoformat(kwargs['updated_at'])
            self.__dict__.update(kwargs)
        else:
            self.id = str(uuid.uuid4())  # creates unique id for each basemodel
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            from .__init__ import storage
            storage.new(self)

    def __str__(self):
        """ print a string representation of the object """
        classy = type(self)
        return ("[{}] ({}) {}".format(classy.__name__, self.id, self.__dict__))

    def save(self):
        """ Updates updated_at with the current datetime """
        self.updated_at = datetime.now()
        from .__init__ import storage
        storage.save()

    def to_dict(self):
        """ returns a dict containting all keys/values of the instance """
        the_dict = dict(self.__dict__)
        the_dict.update({'__class__': type(self).__name__,
                         'updated_at': self.updated_at.isoformat(),
                         'id': self.id,
                         'created_at': self.created_at.isoformat()})
        return the_dict
