from django.contrib import admin
from .models import Order,OrderItems
from table.models import TableName
from django.urls import path
from django.shortcuts import render
from table.models import *
from core.userSession import get_current_user_branch_id

class OrderItemsInline(admin.TabularInline):
    model=OrderItems
    extra=1
    
     


class OrderAdmin(admin.ModelAdmin):
    inlines=[OrderItemsInline]
    readonly_fields=['branch_of',"completion_status"]
    list_display=['id','branch_of','customer','table','user_add','completion_status','created']
    search_fields=['id','customer','code','table']
    list_filter=['created']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "table":
            kwargs["queryset"] = TableName.objects.filter(tcat__branch_of=get_current_user_branch())
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(branch_of=request.user.branch.id )

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser or (obj and obj.branch_of == request.user.branch):
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser or (obj and obj.branch_of == request.user.branch):
            return True
        return False
        
    
    

     

admin.site.register(Order,OrderAdmin)
admin.site.register(OrderItems)
