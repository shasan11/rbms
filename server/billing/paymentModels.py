from django.db import models
from .salesModel import Sales
from core.models import CustomUser
from .salesModel import SalesAmount
from core.userSession import get_current_user
from django.core.exceptions import ValidationError
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import redirect

class PaymentMethod(models.Model):
    id=models.BigAutoField(primary_key=True)
    name=models.CharField(max_length=100,verbose_name="Payment Method")

    class Meta:
        verbose_name='Payment Method'
        verbose_name_plural='Payment Methods'
    
    def __str__(self):
        return self.name


class Payments(models.Model):
    id=models.BigAutoField(primary_key=True,default=222)
    pmethod=models.ForeignKey(PaymentMethod,on_delete=models.PROTECT,verbose_name="Payment Method")
    sid=models.OneToOneField(Sales,on_delete=models.PROTECT,verbose_name="Sales")
    g_amount=models.DecimalField(max_digits=10,decimal_places=2,verbose_name="Recieved Amount")
    r_amount=models.DecimalField(max_digits=10,decimal_places=2,verbose_name="Returned Amount")
    date=models.DateField(auto_now_add=True,verbose_name="TimeStamp")
    user=models.ForeignKey(CustomUser,on_delete=models.PROTECT,verbose_name="Payment Recieved By",default=get_current_user,editable=False)

    class Meta:
        verbose_name='Payment'
        verbose_name_plural='Payments'
    
    def __str__(self):
        return str(self.sid)
    
    def clean(self) -> None:
        sales = SalesAmount.objects.get(sales=self.sid)
        netamt=sales.gtotal
        if netamt>self.g_amount:
            raise ValidationError("The Recieved Amount Must be greater or equal to the net total amount.")
        
        return super().clean()

@receiver(post_save, sender=Payments)
def update_order_paid_status(sender, instance, **kwargs):
    if instance.sid:
        instance.sid.paid_status = True
        instance.sid.save()
        return redirect('render_bill', payment_id=instance.id)
        