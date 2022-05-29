from datetime import datetime
from marshmallow import Schema, fields

class User:
    def __init__(self, name, email) -> None:
        self.name = name
        self.email = email
        self.created_at = datetime.now().date()

    def __repr__(self) -> str:
        return f"<User({self.name})>"

class UserSchema(Schema):
    name = fields.Str()
    email = fields.Email()
    created_at = fields.DateTime()

user = User("laxman","laxman@python.org")
# Serializing object of User into python native datetype
serialized_data = UserSchema().dump(user)
print(serialized_data,type(serialized_data))

# Serialize to Json-encoded string using dumps
json_encoded_data = UserSchema().dumps(user)
print(json_encoded_data, type(json_encoded_data))
