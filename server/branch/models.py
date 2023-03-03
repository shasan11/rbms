from django.db import models

class Branch(models.Model):
    id=models.BigAutoField(primary_key=True,verbose_name="Branch Id")
    name=models.CharField(max_length=100,unique=True,verbose_name="Branch Name")
    seating_capacity=models.PositiveBigIntegerField(verbose_name="Seating Capacity")
    province=models.CharField(max_length=100,verbose_name="Province",null=True)
    district=models.CharField(max_length=100,verbose_name="District",null=True)
    city=models.CharField(max_length=100,verbose_name="City",null=True)
    street_add=models.CharField(max_length=100,verbose_name="Street Address",null=True)
    email=models.EmailField(verbose_name="Email ID",max_length=254,null=True,blank=True)
    phone=models.CharField(verbose_name="Phone Number",max_length=11,null=True,blank=True)
    balance=models.DecimalField(verbose_name="Branch Balance",decimal_places=2,max_digits=10,default=0.00)
    created_at=models.DateTimeField(auto_now_add=True,verbose_name="Created At")
    updated_at=models.DateTimeField(auto_now=True,verbose_name="Updated At")

    class Meta:
        verbose_name = "Branch"
        verbose_name_plural = "Branches"
    
    def __str__(self):
        return str(self.name)


# Create your models here.
