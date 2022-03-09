from distutils.command.upload import upload
from email.mime import image
from django.db import models

# Create your models here.

class product(models.Model):
    product_name=models.CharField(max_length=200)
    price=models.IntegerField()
    quantity=models.IntegerField()
    image=models.ImageField(upload_to="image/",null=True)