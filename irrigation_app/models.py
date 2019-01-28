from django.db import models

# Create your models here.
class CropData(models.Model):
    crop_name = models.CharField(max_length=20,primary_key=True)
    moisture_value = models.FloatField()

    def __str__(self):
        return self.crop_name
