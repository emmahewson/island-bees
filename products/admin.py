from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    """
    Product Model Admin
    """

    readonly_fields = ('rating',)

    list_display = (
        'name',
        'category',
        'rating',
        'price',
        'is_featured',
        'delivery_charge',
        'discontinued',
    )
    list_editable = (
        'is_featured', 'delivery_charge', 'discontinued', 'category')

    ordering = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    """
    Category Model Admin
    """

    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
