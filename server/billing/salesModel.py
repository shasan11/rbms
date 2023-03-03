from django.db import models
from order.models import Order,OrderItems
from django.db.models import Sum
from core.models import CustomUser
from branch.models import Branch
from core.userSession import get_current_user,get_current_user_branch
from django.core.exceptions import ValidationError
from django.db.models.signals import post_save
from django.dispatch import receiver
from .chargeModel import *
import decimal

class Sales(models.Model):
    id=models.BigAutoField(primary_key=True,default=1311)
    branch_of=models.ForeignKey(Branch,on_delete=models.PROTECT,verbose_name="Branch",default=get_current_user_branch,editable=True)
    order=models.ForeignKey(Order,verbose_name="Order",on_delete=models.PROTECT)
    date_created=models.DateTimeField(auto_now_add=True,verbose_name="Date Created")
    dis_amount=models.DecimalField(decimal_places=2,max_digits=10,verbose_name="Discount Amount",default=0.00,editable=False)
    user=models.ForeignKey(CustomUser,on_delete=models.PROTECT,verbose_name="Billed By",default=get_current_user,editable=False)
    paid_status=models.BooleanField(default=False,verbose_name="Paid Status")

    class Meta:
        verbose_name="Create Sale"
        verbose_name_plural="Create Sales"
    
    def __str__(self):
        return  str(self.id)+" "+str(self.order.table)
    
    
    
 
@receiver(post_save, sender=Sales)
def create_sales_items_and_amount(sender, instance, created, **kwargs):
    if created:
        s_a_total =AdditionalCharges.objects.filter(type_charge='A').aggregate(Sum('value'))['value__sum']
        s_p_total =AdditionalCharges.objects.filter(type_charge='P').aggregate(Sum('value'))['value__sum']
        t_a_total =Taxation.objects.filter(type_charge='A').aggregate(Sum('value'))['value__sum']
        t_p_total =Taxation.objects.filter(type_charge='P').aggregate(Sum('value'))['value__sum']

        aa=s_a_total if s_a_total !=None else decimal.Decimal(str(0.00)).quantize(decimal.Decimal('0.01'))
        ap=s_p_total if s_p_total !=None else decimal.Decimal(str(0.00)).quantize(decimal.Decimal('0.01'))

        ta=t_a_total if t_a_total !=None else decimal.Decimal(str(0.00)).quantize(decimal.Decimal('0.01'))
        tp=t_p_total if t_p_total !=None else decimal.Decimal(str(0.00)).quantize(decimal.Decimal('0.01'))

        sub_total=OrderItems.objects.filter(order=instance.order).aggregate(Sum('total'))['total__sum']
        fsub_total=decimal.Decimal(str(sub_total)).quantize(decimal.Decimal('0.01'))  if sub_total !=None else decimal.Decimal(str(0.00)).quantize(decimal.Decimal('0.01'))
        r_taxable=sub_total+aa+(sub_total*(ap/100))
        rtaxes=ta+(fsub_total*(tp/100))
        add=(fsub_total*(ap/100))+aa
         
        a=SalesAmount.objects.create(sales=instance,total=fsub_total,add_charge=add,taxes=rtaxes,taxable=r_taxable)
        a.save()
       


    

class SalesAmount(models.Model):
    id=models.BigAutoField(primary_key=True)
    sales=models.OneToOneField(Sales,on_delete=models.PROTECT,verbose_name="Sales")
    total=models.DecimalField(max_digits=10,decimal_places=2,verbose_name="Total",null=True,blank=True)
    discount=models.DecimalField(max_digits=10,decimal_places=2,verbose_name="Discount",default=0.00)
    add_charge=models.DecimalField(max_digits=10,decimal_places=2,verbose_name="Additional Charges")
    taxable=models.DecimalField(max_digits=10,decimal_places=2,verbose_name="Taxable Amount",blank=True,null=True)
    taxes=models.DecimalField(max_digits=10,decimal_places=2,verbose_name="Taxes")
    gtotal=models.DecimalField(max_digits=10,decimal_places=2,verbose_name="Grand Total",blank=True,null=True)

    class Meta:
        verbose_name="Sale Amount"
        verbose_name_plural="Sales Amounts"
    
    def __str__(self):
        return  str(self.gtotal)

    def save(self, *args, **kwargs):
        self.taxable=self.total+self.add_charge 
        self.gtotal=self.taxable+self.taxes

        super(SalesAmount, self).save(*args, **kwargs)

     
