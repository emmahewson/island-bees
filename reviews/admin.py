from django.contrib import admin
from .models import Review


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


admin.site.register(Review, ReviewAdmin)
