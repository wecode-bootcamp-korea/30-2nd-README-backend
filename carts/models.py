from django.db import models

from utils.time_stamp_model import TimeStampModel
class Cart(TimeStampModel):
    user    = models.ForeignKey('users.User', on_delete=models.CASCADE)
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)

    class Meta:
        db_table = 'carts'


class CartSeries(TimeStampModel):
    cart   = models.ForeignKey('Cart', on_delete=models.CASCADE)
    series = models.ForeignKey('products.Series', on_delete=models.CASCADE)

    class Meta:
        db_table = 'cart_series'
