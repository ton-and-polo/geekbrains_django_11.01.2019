from django.db import models
from django.urls import reverse

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10000, decimal_places=2)
    image = models.ImageField(
        blank=True,
        null=True
    )
    description = models.TextField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse("products:product-details", kwargs={"id": self.id})