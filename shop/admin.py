from django.contrib import admin
from .models import Product, Categories, Orders, MediaTest


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Categories, CategoriesAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'slug', 'price','created_date', 'in_stock']
    list_filter = ['in_stock', 'is_active']
    list_editable = ['price','created_date', 'in_stock']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Product, ProductAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = ['item','quantity', 'price', 'name', 'email', 'city','state']
    list_filter = ['city', 'state']

admin.site.register(Orders, OrderAdmin)

class MediaTestAdmin(admin.ModelAdmin):
    list_display = ['description','image_details']

admin.site.register(MediaTest, MediaTestAdmin)
