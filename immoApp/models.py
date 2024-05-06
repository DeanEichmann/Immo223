from django.db import models

# Create your models here.
class estate(models.Model):

    def __str__(self):
        return self.estate_name

    estate_name = models.CharField(max_length=200)
    estate_description = models.CharField(max_length=1000)