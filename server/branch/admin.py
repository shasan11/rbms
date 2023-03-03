from django.contrib import admin
from .models import Branch

class BranchAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','seating_capacity','province','district','city','street_add',"created_at","updated_at"]
    list_display_links = ['name']
    ordering=['id']
    search_fields = ['name', 'id','location']

admin.site.register(Branch,BranchAdmin)


# Register your models here.
