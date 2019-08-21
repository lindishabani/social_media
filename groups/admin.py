from django.contrib import admin
from . import models


class GroupMemberInLine(admin.TabularInline):
    model = models.GroupMembers


admin.site.register(models.Group)

