from django.contrib import admin

# Register your models here.
from webapp.models import Product, Review


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category']
    list_filter = ['category']
    search_fields = ['category']
    fields = ['id', 'name', 'description', 'category', 'image']
    readonly_fields = ['id']

admin.site.register(Product, ProductAdmin)
admin.site.register(Review)