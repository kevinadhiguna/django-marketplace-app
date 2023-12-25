from django.contrib import admin

from .models import Category

# Register your models here.
admin.site.register(Category) # In order to show 'Category' model in the admin panel
