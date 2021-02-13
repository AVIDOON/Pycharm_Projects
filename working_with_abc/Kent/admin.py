from django.contrib import admin
from .models import Products
from .models import NewProducts


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


class NewProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


admin.site.register(Products,ProductAdmin)
admin.site.register(NewProducts,NewProductAdmin)
