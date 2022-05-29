from datetime import datetime
from marshmallow import Schema, fields, post_load

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
