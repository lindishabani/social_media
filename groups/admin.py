from django.contrib import admin
from . import models


class GroupMemberInLine(admin.TabularInline):
    model = models.GroupMembers


class GroupAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'description', 'description_html')
    list_display_links = ('name',)
    list_filter = ('name',)
    search_fields = ('name', 'slug')


admin.site.register(models.Group, GroupAdmin)

