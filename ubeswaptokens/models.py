from django.db import models

# Create your models here.
class UbeswapModels(models.Model):
    ubetokenlogourl = models.URLField(max_length=1000)
    ubetokenname = models.CharField(max_length=1000)
    uberewards = models.FloatField()
    ubeprice = models.FloatField()

    def __str__(self):
        return self.ubetokenname