from django.contrib import admin
from menu.models import MenuItems
from django.shortcuts import render
from django.db.models import Sum
from decimal import Decimal
from billing.chargeModel import *
from .chargeModel import *
from .salesModel import *
from . paymentAdmin import PaymentAdmin
from core.userSession import *
class ChargeAdmin(admin.ModelAdmin):
    list_display=['name','type_charge','value']
    search_fields=['name']
    extra=1
admin.site.register(AdditionalCharges,ChargeAdmin)

class ChargeAdmin(admin.ModelAdmin):
    list_display=['name','type_charge','value']
    search_fields=['name']
    extra=1
admin.site.register(Taxation,ChargeAdmin)

class SalesAmountAdmin(admin.StackedInline):
    model=SalesAmount
    extra=5
    model=SalesAmount
    readonly_fields = ['total',"discount",'add_charge','taxable','taxes','gtotal']
    extra=5

class SalesAdmin(admin.ModelAdmin):
     
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(branch_of=request.user.branch )

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser or (obj and obj.branch_of == request.user.branch):
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser or (obj and obj.branch_of == request.user.branch):
            return True
        return False

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "order":
            kwargs["queryset"] = Order.objects.filter(branch_of=request.user.branch.id,completion_status=False).all()
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    

    
    list_display=['id','branch_of','order','date_created','user']
    search_fields=['id']
    list_filter=['date_created']
    
    inlines=[SalesAmountAdmin,PaymentAdmin]

    exclude = ('paid_status',)
       
    
admin.site.register(Sales,SalesAdmin)
admin.site.register(SalesAmount)

 

# Register your models here.
