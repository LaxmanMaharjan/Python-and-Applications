from marshmallow import Schema, fields
from datetime import datetime

class UserSchema(Schema):
    name = fields.Str()
    email = fields.Email()
    created_at = fields.DateTime()

user_data = {
        "name":"laxman",
        "email":"laxman@python.org",
        "created_at":str(datetime.now())
        }

# deserialize the data structure to an object defined by Schema's fields
deserialized_data = UserSchema().load(user_data)
print(deserialized_data, type(deserialized_data))
print(type(deserialized_data["name"]))
print(type(deserialized_data['email']))
print(type(deserialized_data['created_at']))
