from marshmallow import Schema, fields, post_load
from datetime import datetime

class User:
    def __init__(self, name, email) -> None:
        self.name = name
        self.email = email
        self.created_at = datetime.now().date()

    def __repr__(self) -> str:
        return f"<User({self.name},{self.email},{self.created_at})>"

class UserSchema(Schema):
    name = fields.Str()
    email = fields.Email()
    created_at = fields.DateTime()

    @post_load
    def make_user(self, data, **kwargs):
        return User(**data)

user_data = {
        "name":"laxman",
        "email":"laxman@python.org",
        }

# deserialize the data structure to an User object
deserialized_data = UserSchema().load(user_data)
print(deserialized_data, type(deserialized_data))
