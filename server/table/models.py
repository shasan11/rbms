from django.db import models
from branch.models import Branch
from django.conf import settings
from core.userSession import get_current_user_branch



class TableCategory(models.Model):
    id=models.BigAutoField(primary_key=True)
    branch_of=models.ForeignKey(Branch,on_delete=models.CASCADE,verbose_name="Branch",editable=False,default=get_current_user_branch)
    name=models.CharField(max_length=100,verbose_name="category Name")
    desc=models.TextField(verbose_name="Description",blank=True,null=True)

     
        
    class Meta:
        verbose_name="Table"
        verbose_name_plural="Tables"
    
    def __str__(self):
        return self.name
    
    

class TableName(models.Model):
    id=models.BigAutoField(primary_key=True)
    tcat=models.ForeignKey(TableCategory,on_delete=models.CASCADE,verbose_name="Table Category")
    name=models.CharField(max_length=100,verbose_name="Table Name")
    desc=models.TextField(verbose_name="Description",blank=True,null=True)
    res_status=models.BooleanField(default=False,verbose_name="Reserved/Taken")

    class Meta:
        verbose_name="Table"
        verbose_name_plural="Tables"
    
    def __str__(self):
        return self.name
# Create your models here.
