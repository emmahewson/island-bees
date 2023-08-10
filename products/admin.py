from django.contrib import admin
from .models import Product, Category, Review

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'price',
        'image',
        'is_featured',
    )
    list_editable = ('is_featured',)

    ordering = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'user',
        'title',
        'rating',
        'created_on',
        'is_featured'
    )
    list_editable = ('is_featured',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Review, ReviewAdmin)
