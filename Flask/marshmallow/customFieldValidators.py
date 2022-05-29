from marshmallow import Schema, fields, validates
from marshmallow.exceptions import ValidationError

class ItemSchema(Schema):
    quantity = fields.Integer()

    @validates('quantity')
    def validate_quantity(self, value):
        if value < 0:
            raise ValidationError("Quantity must be greater than zero.")
        if value > 30:
            raise ValidationError("Quantity must be less than Thirty.")
