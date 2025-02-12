from django.db import models

# Create your models here.
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    year = models.IntegerField()
    author = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    title = models.CharField(max_length=30)
    synopsis = models.TextField()