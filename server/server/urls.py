from django.contrib import admin
from django.urls import path,include
from core.views import index
from billing.views import render_bill
 
urlpatterns = [
    path('render_bill/',render_bill),
    path('', admin.site.urls),    
    
]
