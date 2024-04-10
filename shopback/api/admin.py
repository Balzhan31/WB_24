from django.contrib import admin
from .models import Category, Product

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name', 'id')
    ordering = ('id',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'description', 'count', 'is_active', 'category_id')
    search_fields = ('name', 'id')
    ordering = ('id',)
