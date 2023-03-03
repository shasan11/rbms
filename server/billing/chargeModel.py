from django.db import models

class AdditionalCharges(models.Model):
    id=models.BigAutoField(primary_key=True)
    name=models.CharField(max_length=100,verbose_name="Charge Name")
    type_charge=models.CharField(max_length=100,verbose_name="Type",choices=(("A","Amount"),("P","Percent")))
    value=models.DecimalField(max_digits=10,decimal_places=2,verbose_name="Value")
    def __str__(self):
        return self.name

    class Meta:
        verbose_name="Additional Charge"
        verbose_name_plural="Additional Charges"

class Taxation(models.Model):
    id=models.BigAutoField(primary_key=True)
    name=models.CharField(max_length=100,verbose_name="Charge Name")
    type_charge=models.CharField(max_length=100,verbose_name="Type",choices=(("A","Amount"),("P","Percent")))
    value=models.DecimalField(max_digits=10,decimal_places=2,verbose_name="Value")   
    def __str__(self):
        return self.name

    class Meta:
        verbose_name="Tax Charge"
        verbose_name_plural="Tax Charges"