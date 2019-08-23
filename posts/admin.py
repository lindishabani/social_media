from django.contrib import admin
from . import models


class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'message', 'message_html', 'group')
    list_display_links = ('user', 'message')
    list_filter = ('user',)
    search_fields = ('user', 'group', 'message')


admin.site.register(models.Post, PostAdmin)
