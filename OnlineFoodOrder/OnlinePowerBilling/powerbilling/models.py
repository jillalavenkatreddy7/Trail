from django.db import models

# Create your models here.
class OnlinePower(models.Model):
    meter_number=models.IntegerField(primary_key=True)
    customer_name=models.CharField(max_length=50)
    Meter_type=models.CharField(max_length=50)
    units=models.DecimalField(max_digits=10,decimal_places=2)
    Per_unit=models.DecimalField(max_digits=10,decimal_places=2)
    total=models.DecimalField(max_digits=10,decimal_places=2)

