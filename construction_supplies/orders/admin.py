from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Product)
class productAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'category', 'supplier', 'image')