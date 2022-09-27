from tortoise import fields, models


class CityBikeStation(models.Model):
    """
    The CityBikeStation model
    """
    id = fields.BigIntField(pk=True)
    station_id = fields.IntField()
    name = fields.CharField(max_length=100)
    active = fields.BooleanField()
    description = fields.TextField()
    boxes = fields.IntField()
    free_boxes = fields.IntField()
    free_bikes = fields.IntField()
    longitude = fields.DecimalField(max_digits=50, decimal_places=15)
    latitude = fields.DecimalField(max_digits=50, decimal_places=15)
    internal_id = fields.IntField()
    created_at = fields.DatetimeField(auto_now_add=True)

    addresses: fields.ReverseRelation["models.Address"]

    def __str__(self):
        return f"{self.name}"

    @property
    def free_ratio(self):
        if self.boxes > 0:
            return self.free_boxes / self.boxes

    @property
    def coordinates(self):
        return [self.longitude, self.latitude]
