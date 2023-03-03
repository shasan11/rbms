from django.db import models
from branch.models import Branch

class MenuCategory(models.Model):
    id=models.BigAutoField(primary_key=True)
    name=models.CharField(unique=True,verbose_name="Category Name",max_length=100)
    desc=models.TextField(verbose_name="Description",blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True,verbose_name="Created At")
    updated_at=models.DateTimeField(auto_now=True,verbose_name="Updated At")

    class Meta:
        verbose_name="Menu"
        verbose_name_plural="Menus"

    def __str__(self):
        return self.name

class MenuItems(models.Model):
    id=models.BigAutoField(primary_key=True)
    menucat=models.ForeignKey(MenuCategory,on_delete=models.CASCADE,verbose_name="Menu Category")
    name=models.CharField(unique=True,verbose_name="Name",max_length=100)
    price=models.DecimalField(max_digits=10,decimal_places=2,verbose_name="Unit Price")
    desc=models.TextField(verbose_name="Description",blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True,verbose_name="Created At")
    updated_at=models.DateTimeField(auto_now=True,verbose_name="Updated At")

    class Meta:
        verbose_name="Menu Item"
        verbose_name_plural="Menu Items"

    def __str__(self):
        return self.name

    


# Create your models here.
