from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator

class Size(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return "{}".format(self.name)

class Gluten(models.Model):
    name = models.BooleanField()

    def __str__(self):
        return "{}".format(self.name)

class Crust(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return "{}".format(self.name)

class Sauce(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return "{}".format(self.name)

class Cheese(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return "{}".format(self.name)

class Topping(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return "{}".format(self.name)

class Pizza(models.Model):
    id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(User, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    crust = models.ForeignKey(Crust, on_delete=models.CASCADE)
    gluten = models.ForeignKey(Gluten, on_delete=models.CASCADE)
    sauce = models.ForeignKey(Sauce, on_delete=models.CASCADE)
    cheese = models.ForeignKey(Cheese, on_delete=models.CASCADE)
    toppings = models.ForeignKey(Topping, null=True, on_delete=models.CASCADE)
    additional_notes = models.TextField(default='no other instructions')
    ordertime = models.DateTimeField()
    deliverytime = models.DateTimeField(null=True, blank=True, default=None)

    def __str__(self):
        return "Order Number {}".format(self.id)

    def save(self, *args, **kwargs):
        self.deliverytime = self.ordertime + timedelta(minutes=40)
        return super().save(*args, **kwargs)
    
class Payment_Details(models.Model):
    #order_id = models.IntegerField()
    name = models.CharField(max_length=50)
    address = models.TextField()
    card_number = models.IntegerField(validators=[MaxValueValidator(9999999999999999)]) 
    # 4 groups of 4 digits, the format of bank cards
    
    cvv = models.IntegerField(validators=[MaxValueValidator(999)])
    # limits cvv to 3 digits
    card_expiry = models.DateField() # you apparantly revise this with bootstrap



