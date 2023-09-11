from django.contrib import admin
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    fields = ('user', 'default_phone_number', 'default_country',
              'default_postcode', 'default_town_or_city',
              'default_street_address1', 'default_street_address2',
              'default_county')

    list_display = ('user', 'default_phone_number', 'default_country',
                    'default_postcode', 'default_town_or_city',
                    'default_street_address1', 'default_street_address2',
                    'default_county')


admin.site.register(UserProfile, UserProfileAdmin)