from django.contrib import admin
from basic_app import models
# Register your models here.

admin.site.register(models.SchoolModel)
admin.site.register(models.StudentModel)
