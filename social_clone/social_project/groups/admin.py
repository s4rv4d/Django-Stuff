from django.contrib import admin
from . import models
# Register your models here.

#this is to make sure that group members can be edited in admin site
class GroupMemberInline(admin.TabularInline):
    model = models.GroupMember

admin.site.register(models.Group)
