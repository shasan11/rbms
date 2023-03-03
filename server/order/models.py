from django.db import models
from branch.models import Branch
from table.models import TableName
from customers.models import Customer 
from core.models import CustomUser
from menu.models import MenuItems 
from core.userSession import get_current_user,get_current_user_branch 
 


order_choices=(
    ("P","Pending"),
    ("C","Confirmed"),
    ("IP","In Progress"),
    ("R","Ready"),
    ("D","Delivered"),
    ("CC","Cancelled")
)

class Order(models.Model):
    id=models.BigAutoField(primary_key=True,default=231)
    branch_of=models.ForeignKey(Branch,on_delete=models.CASCADE,verbose_name="Branch",related_name="branch_name",editable=False,default=get_current_user_branch)
    customer=models.ForeignKey(Customer,on_delete=models.PROTECT,verbose_name="Customer",blank=True,null=True)
   # code=models.CharField(max_length=5, unique=True, default=shortuuid.ShortUUID().random(length=5),verbose_name="Order No",editable=False)
    table=models.ForeignKey(TableName,on_delete=models.CASCADE,verbose_name="Table",blank=True,null=True,related_name="table_name",)
    user_add=models.ForeignKey(CustomUser,on_delete=models.PROTECT,verbose_name="Order Opened By",editable=False,null=True,default=get_current_user)
    completion_status=models.BooleanField(default=False,verbose_name="Completed")
    created=models.DateTimeField(auto_now_add=True,verbose_name="Time")

    def save(self, *args, **kwargs):
        tbl=TableName.objects.get(id=self.table.pk)
        tbl.res_status=True
        super(Order, self).save(*args, **kwargs)

    def __str__(self):
        return  str(self.table)

    class Meta:
        verbose_name="Order"
        verbose_name_plural="Orders"

    def get_formset(self, request, obj=None, **kwargs):
        formset = super().get_formset(request, obj, **kwargs)
        if obj:
            formset.queryset = formset.queryset.filter(parent=obj)
        else:
            formset.queryset = formset.queryset.none()
        return formset

class OrderItems(models.Model):
    id=models.BigAutoField(primary_key=True)
    order=models.ForeignKey(Order,on_delete=models.CASCADE,verbose_name="Order")
    food_item=models.ForeignKey(MenuItems,on_delete=models.PROTECT,verbose_name="Item")
    qty=models.PositiveSmallIntegerField(verbose_name="Quantity")
    total=models.DecimalField(max_digits=10,decimal_places=2,verbose_name="Total",editable=False,null=True,blank=True)
    desc=models.TextField("Description",blank=True,null=True)
    timestamp=models.DateTimeField(verbose_name="Time Stamp",auto_now_add=True)
    user_add=models.ForeignKey(CustomUser,on_delete=models.PROTECT,verbose_name="Order taken by",editable=False,null=True,default=get_current_user)

    def __str__(self):
        return str(self.id)
    
    def save(self, *args, **kwargs):
        menu_item=MenuItems.objects.get(id=self.food_item.pk)
        price=menu_item.price
        self.total = price * self.qty
        super(OrderItems, self).save(*args, **kwargs)
     
        

    class Meta:
        verbose_name="Order Item"
        verbose_name_plural="Order Items"
    
