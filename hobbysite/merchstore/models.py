from django.db import models
from user_management.models import Profile

class ProductType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    class Meta:
        ordering = ['name']

class Product(models.Model):
    STATUS_CHOICES = {'Available':'Available', 
        'On sale':'On sale', 
        'Out of stock':'Out of stock'}

    name = models.CharField(max_length=255)
    product_type = models.ForeignKey(ProductType, null=True, on_delete=models.SET_NULL)
    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL, related_name="product")
    description = models.TextField()
    price = models.DecimalField(max_digits=99, decimal_places=2)
    stock = models.IntegerField()
    status = models.CharField(max_length=255, default="Available", choices=STATUS_CHOICES)

    def save(self, *args, **kwargs):
        if self.stock <= 0:
            self.status = "Out of stock"
        super(Product, self).save(*args, **kwargs)

    class Meta:
        ordering = ['name']

class Transaction(models.Model):
    buyer = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL, related_name="transaction")
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL, related_name="transaction")
    amount = models.IntegerField()
    status = models.CharField(max_length=255, default="On cart")
    created_on = models.DateTimeField(auto_now_add=True)
