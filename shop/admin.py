from django.contrib import admin
from .models import Product, Categories


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
