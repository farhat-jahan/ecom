from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
import datetime



class Base(models.Model):
    id = models.AutoField(primary_key=True)
    created_date = models.DateField(default=timezone.now())

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
    discount = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='shop/images/')
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    modified_date = models.DateField(datetime.datetime.now())

    class Meta:
        db_table = 'product'

    def __str__(self):
        return self.title


class Orders(Base):
    item = models.CharField(max_length=1000)
    quantity = models.CharField(max_length=20, null=False)
    price = models.CharField(max_length=40, default=0)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)

    class Meta:
        db_table = 'orders'

    def __str__(self):
        return self.item


