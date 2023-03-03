from django.shortcuts import render
from order.models import OrderItems
from billing.salesModel import *
from billing.paymentModels import *
from billing.chargeModel import *
import datetime
def render_bill(request, payment_id):
    payment = Payments.objects.get(id=payment_id)
    salesobj=payment.sid,
    sales_amount=SalesAmount.objects.get(sales=salesobj)
    order_items=OrderItems.objects.filter(order=salesobj.order)  
    current_date = datetime.date.today() 
    context = {'payment': payment,'sales_amount':sales_amount,'order_items':order_items,'sales':salesobj,'currentdate':current_date}
    return render(request, 'bill_template.html', context)


# Create your views here.
