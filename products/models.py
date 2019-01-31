from django.db import models
from django.urls import reverse

# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10000, decimal_places=2)
    image = models.ImageField(
        upload_to='products_img/',
        blank=True,
        null=True
    )
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("products:product-details", kwargs={"id": self.id})