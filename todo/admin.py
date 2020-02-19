from django.contrib import admin
from .models import Item

# Register your models here.
# This will register the item in the admin side
admin.site.register(Item)