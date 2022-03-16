from django.db              import models

from utils.time_stamp_model import TimeStampModel

class Product(TimeStampModel):
    name         = models.CharField(max_length=45)
    description  = models.TextField()
    publisher    = models.ForeignKey('Publisher', on_delete=models.CASCADE)
    translator   = models.ForeignKey('Translator', on_delete=models.CASCADE)
    author       = models.ForeignKey('Author', on_delete=models.CASCADE)
    category     = models.ForeignKey('Category', on_delete=models.CASCADE)

    class Meta:
        db_table = 'products'

class Translator(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'translators'

class Author(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'authors'

class Publisher(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'publishers'

class Image(models.Model):
    image_url = models.URLField(max_length=2000)
    product   = models.ForeignKey('Product', on_delete=models.CASCADE)

    class Meta:
        db_table = 'images'

class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'categories'
        
class Series(models.Model):
    name         = models.CharField(max_length=100)
    price        = models.DecimalField(max_digits=10, decimal_places=2)
    sequence     = models.PositiveSmallIntegerField()
    published_at = models.DateField()
    product      = models.ForeignKey('Product', on_delete=models.CASCADE)

    class Meta:
        db_table = 'series'