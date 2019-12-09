from django.conf import settings


class User:

    table = "stu"
    db = settings.MONGO_CLIENT.fortest

    @classmethod
    def insert(cls, **params):
        return cls.db[cls.table].insert(params)

    @classmethod
    def get(cls, **params):
        return cls.db[cls.table].find(params)

    @classmethod
    def get_one(cls, **params):
        return cls.db[cls.table].find_one(params)

    @classmethod
    def update(cls, _id, **params):
        cls.db[cls.table].update({"_id": _id}, {"$set": params})
