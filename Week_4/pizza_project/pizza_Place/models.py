from django.db import models

class Size(models.Model):
    size = models.CharField(max_length=20)

    def __str__(self):
        return "{}".format(self.size)

class Gluten(models.Model):
    gluten = models.BooleanField()

    def __str__(self):
        return "{}".format(self.gluten)

class Crust(models.Model):
    thickness = models.CharField(max_length=20)

    def __str__(self):
        return "{}".format(self.thickness)

class Sauce(models.Model):
    sauce = models.CharField(max_length=20)

    def __str__(self):
        return "{}".format(self.sauce)

class Cheese(models.Model):
    cheese = models.CharField(max_length=50)

    def __str__(self):
        return "{}".format(self.cheese)

class Topping(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return "{}".format(self.name)

class Pizza(models.Model):
    id = models.AutoField(primary_key=True)
    #customer_id = models.IntegerField()
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    crust = models.ForeignKey(Crust, on_delete=models.CASCADE)
    gluten = models.ForeignKey(Gluten, on_delete=models.CASCADE)
    sauce = models.ForeignKey(Sauce, on_delete=models.CASCADE)
    cheese = models.ForeignKey(Cheese, on_delete=models.CASCADE)
    toppings = models.ForeignKey(Topping, on_delete=models.CASCADE)
    additional_notes = models.TextField()

class Payment_Details(models.Model):
    #order_id = models.IntegerField()
    name = models.CharField(max_length=50)
    address = models.TextField()
    card_number = models.IntegerField()
    cvv = models.IntegerField()
    card_expiry = models.DateField() # needs a complete date, will revise



