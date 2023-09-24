from django.contrib import admin
from .models import Message


class MessageAdmin(admin.ModelAdmin):
    """
    Message Model Admin
    """

    readonly_fields = ('created_on',)

    list_display = (
        'name',
        'subject',
        'created_on',
        'is_open',
    )

    list_editable = ('is_open',)


admin.site.register(Message, MessageAdmin)
