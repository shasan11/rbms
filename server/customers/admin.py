from django.contrib import admin
from . models import Customer
class CustomerAdmin(admin.ModelAdmin):
    list_display=['first_name','last_name','email','phone_number','address','city','state','zip_code']
    search_fields=list_display

# Register your models here.
admin.site.register(Customer,CustomerAdmin)