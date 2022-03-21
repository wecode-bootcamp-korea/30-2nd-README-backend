from django.db              import models

from utils.time_stamp_model import TimeStampModel

class User(TimeStampModel):
    nickname      = models.CharField(max_length=45)
    date_of_birth = models.DateField(null=True, blank=True)
    gender        = models.ForeignKey('Gender', on_delete=models.CASCADE)
    kakao_id      = models.CharField(max_length=100)
    point         = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'users'

class Gender(models.Model):
    sex = models.CharField(max_length=10)

    class Meta:
        db_table = 'gender'
