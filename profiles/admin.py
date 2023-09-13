from django.contrib import admin
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    fields = (
        'user', 'default_street_address1', 'default_street_address2',
        'default_town_or_city', 'default_county', 'default_postcode',
        'default_country', 'default_phone_number',)

    list_display = (
        'user', 'default_street_address1', 'default_street_address2',
        'default_town_or_city', 'default_county', 'default_postcode',
        'default_country', 'default_phone_number',)


admin.site.register(UserProfile, UserProfileAdmin)
