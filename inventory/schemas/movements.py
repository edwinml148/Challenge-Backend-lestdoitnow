from marshmallow import Schema, fields, validate


class LotSchema(Schema):
    lot_id = fields.String(validate=validate.Length(max=200), required=True)
    due_date = fields.DateTime()
    product = fields.Integer(default=None, required=True)

class ProductDetailsSchema(Schema):
    product = fields.Integer(default=None, required=True)
    description = fields.String(validate=validate.Length(max=200), required=True)
    product_qty = fields.Integer(default=None, required=True)
    lot = fields.Nested(LotSchema)


class ProductsDetailsSchema(Schema):
    product_details = fields.List(fields.Nested(ProductDetailsSchema), required=True)