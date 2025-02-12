from django.db import models

#customer model
class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=15)
    #email = models.CharField(max_length=20)
    #2password = models.CharField(max_length=50)
    address = models.TextField()

class Size(models.Model):
    size = models.CharField(max_length=20)

class Crust(models.Model):
    thickness = models.CharField(max_length=20)
    gluten = models.BooleanField()

class Sauce(models.Model):
    sauce = models.CharField(max_length=20)

class Cheese(models.Model):
    cheese = models.CharField(max_length=50)

class Toppings(models.Model):
    name = models.CharField(max_length=20)

class Pizza(models.Model):
    order_number = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
"""""
class Pizza(models.Model)
    order_number = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    size = #small, med, large, xl, mega
    crust = #thin, normal, thick, stuffed, 
    gluten_free = 
    sauce = #tomato, bbq, 
 
    additional_notes = models.Textfield()
    # method is either collection or delivery
    # so a boolean field works to define this
    # true = delivery
    method =  models.BooleanField()
    payment_method = 
"""""
