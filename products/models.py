import uuid

from django.db import models
from django.urls import reverse

from .validators import validate_box_size, validate_article_number
from cloudinary.models import CloudinaryField


# Create your models here.

class Age(models.Model):
    """
    Model for Age Types
    """
    uuid = models.UUIDField(default=uuid.uuid4(), editable=False)
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Product(models.Model):
    """
    Model for Product
    """
    uuid = models.UUIDField(default=uuid.uuid4(), editable=False)
    title = models.CharField(max_length=200, null=False)
    description = models.TextField(max_length=1200, null=False)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=False)
    article_number = models.TextField(max_length=50, blank=True, validators=[validate_article_number])
    box_size = models.CharField(max_length=50, blank=True, validators=[validate_box_size])
    for_age = models.ForeignKey('Age', on_delete=models.CASCADE)
    image = CloudinaryField('image')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"uuid": self.uuid})
