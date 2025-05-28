#!/usr/bin/python3
""" defines all common attributes/methods for other classes """
import uuid
import datetime


class BaseModel:
    """ define the attributes of the base model """
    def __init__(self):
        """ initialize the basemodel when called """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """ returns  [<class name>] (<self.id>) <self.__dict__> """
        return f"[{(type(self)).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ update the instance with current datetime """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """
        returns a dictionary containing all
        keys/values of __dict__ of the instance
        """
        new = self.__dict__
        newer = {}
        for key, value in new.items():
            if key == 'created_at' or key == 'updated_at':
                newer[key] = value.isoformat()
                continue
            newer[key] = value
        newer['__class__'] = __class__.__name__
        return newer
