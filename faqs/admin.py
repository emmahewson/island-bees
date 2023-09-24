from django.contrib import admin
from .models import Faq


class FaqAdmin(admin.ModelAdmin):
    """
    FAQ Model Admin
    """
    list_display = (
        'question',
        'answer',
    )


admin.site.register(Faq, FaqAdmin)
