from django.contrib import admin
from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    """
    Review Model Admin
    """

    list_display = (
        'product',
        'user',
        'title',
        'rating',
        'created_on',
        'is_approved',
    )

    list_editable = ('is_approved',)


admin.site.register(Review, ReviewAdmin)
