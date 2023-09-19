from django.contrib import admin
from .models import Product, Category

# Register your models here.


class ProductAdmin(admin.ModelAdmin):

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
    list_editable = ('is_featured', 'delivery_charge', 'discontinued')

    ordering = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
