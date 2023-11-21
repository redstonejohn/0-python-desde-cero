from django.db import models

# Create your models here.

class articulos(models.Model):
    
    title = models.TextField(max_length=200)
    price = models.FloatField()
    description = models.TextField(max_length=1000)
    category = models.TextField(max_length=200)
    image = models.TextField(max_length=1000)

class ratings(models.Model):
    rate = models.FloatField()
    count = models.IntegerField()
    articulo = models.ForeignKey(articulos, on_delete=models.CASCADE)


"""     
Tabla producto
Id int
Title string
Price float
Description string
Category string
Image string

Tabla rating
Id int
Rate float
count int """