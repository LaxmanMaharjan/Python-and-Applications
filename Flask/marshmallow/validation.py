from marshmallow import Schema, fields, validate

class UserSchema(Schema):
    name = fields.Str(validate=validate.Length(min = 1))
    permission = fields.Str(validate=validate.OneOf(['read','write','admin']))
    age = fields.Int(validate=validate.Range(min=18,max=40))

in_data = {'name':"",'permission':'invalid','age':71}

try:
    UserSchema().load(in_data)
except Exception as e:
    print(e)

