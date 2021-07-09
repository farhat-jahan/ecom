from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
import datetime



class Base(models.Model):
    id = models.AutoField(primary_key=True)
    created_date = models.DateField(timezone.now())

    class Meta:
        abstract = True


class Categories(Base):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        db_table = 'categories'

    def __str__(self):
        return self.name


class Product(Base):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, default='admin')
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/')
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    modified_date = models.DateField(datetime.datetime.now())

    class Meta:
        db_table = 'product'

    def __str__(self):
        return self.title

