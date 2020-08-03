from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Products(models.Model):
    CATEGORY = (
        ("Indoor","Indoor"),
        ("Outdoor", "Outdoor"),
        )
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(max_length=200, null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True)


class Order(models.Model):
    STATUS = (
            ("Pending", "Pending"),
            ("Out for delivery", "Out for delivery"),
            ("Delivered","Delivered")
            )
    #customer =
    #products =
    date_created = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=200, null=True, choices=STATUS)
    