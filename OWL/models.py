from django.db import models

# Create your models here.
class Soldier(models.Model):
    phone = models.CharField(max_length=15)
    carrier = models.CharField(max_length=100)
    join_date = models.DateTimeField('date joined')
    zip_code = models.IntegerField(default=0)
    active = models.IntegerField(default=0)
