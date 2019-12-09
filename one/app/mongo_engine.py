from mongoengine import connect, Document, StringField, IntField, ReferenceField


# connect('fortest', host="localhost", port=27017, username="admin", password="1234")
connect(host="mongodb://admin:1234@localhost:27017/fortest?authSource=admin")


class Users(Document):
    name = StringField(required=True, max_length=200)
    age = IntField(required=True)


class Paper(Document):
    title = StringField(required=True, max_length=200)
    user = ReferenceField(Users)
