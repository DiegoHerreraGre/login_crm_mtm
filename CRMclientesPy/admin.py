from django.contrib import admin
from django.utils.html import format_html

from .models import Record


class RecordAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number', 'city', 'state', 'avatar_image')

    def avatar_image(self, obj):
        return format_html('<img src="{}" width="50" height="50" />', obj.avatar.url)

    avatar_image.short_description = 'Avatar'


admin.site.register(Record, RecordAdmin)
