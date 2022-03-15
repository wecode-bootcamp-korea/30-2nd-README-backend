from django.db              import models

from utils.time_stamp_model import TimeStampModel

class Review(TimeStampModel):
    content = models.TextField()
    rating  = models.FloatField()
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    user    = models.ForeignKey('users.User', on_delete=models.CASCADE)

    class Meta:
        db_table = 'reviews'

class Like(models.Model):
    user   = models.ForeignKey('users.User', on_delete=models.CASCADE)
    review = models.ForeignKey('Review', on_delete=models.CASCADE)

    class Meta:
        db_table = 'likes'
