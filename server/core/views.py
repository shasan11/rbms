from django.shortcuts import render
from core.userSession import get_current_user_branch
from table.models import *
def index(request):
    branch_res=get_current_user_branch()
    table_cat=TableCategory.objects.filter(branch_of=branch_res)
    table_name=TableName.objects.filter(tcat=table_cat).all
    return render(request,"index.html",{'table': table_name})
# Create your views here.
