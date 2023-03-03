from django.contrib import admin
from django.db.models import Sum
from decimal import Decimal
from billing.chargeModel import *
from .chargeModel import *
from .salesModel import *
from .paymentModels import * 
import datetime
today = datetime.date.today()

admin.site.register(PaymentMethod)

class PaymentAdmin(admin.StackedInline):
    model=Payments
    
 
    

