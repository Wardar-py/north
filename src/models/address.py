from tortoise import fields, models


class Address(models.Model):
    """
    The Address model
    """
    id = fields.BigIntField(pk=True)
    longitude = fields.DecimalField(max_digits=50, decimal_places=15)
    lontitude = fields.DecimalField(max_digits=50, decimal_places=15)
    type = fields.CharField(max_length=25)
    name = fields.CharField(max_length=100)
    address_id = fields.TextField()
    station = fields.ForeignKeyField("models.CityBikeStation", related_name="addresses")
