from django.db import models

from utils.time_stamp_model import TimeStampModel

class Order(TimeStampModel):
    order_number = models.UUIDField()
    user         = models.ForeignKey('users.User', on_delete=models.CASCADE)
    product      = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    series       = models.ForeignKey('products.Series', on_delete=models.CASCADE)

    class Meta:
        db_table = 'orders'
        