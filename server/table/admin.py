from django.contrib import admin
from . models import *

class TableInline(admin.StackedInline):
    model = TableName
    extra = 3 
    search_fields=('name',)

@admin.register(TableCategory)
class TableNameAdmin(admin.ModelAdmin):
    list_display=["branch_of","name","desc"]
    inlines = [TableInline]
    search_fields=('name',"branch_of",)
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(branch_of=request.user.branch)

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser or (obj and obj.branch_of== request.user.branch):
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser or (obj and obj.branch_of == request.user.branch):
            return True
        return False
# Register your models here.
