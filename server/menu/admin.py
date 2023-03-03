from django.contrib import admin
from .models import *

class MenuItemsInline(admin.StackedInline):
    model=MenuItems
    extra=5

class MenuCatInline(admin.ModelAdmin):
    model=MenuCategory
    inlines=[MenuItemsInline]

admin.site.register(MenuCategory,MenuCatInline)
# Register your models here.
