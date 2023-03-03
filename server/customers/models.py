from django.db import models

class Customer(models.Model):
    id=models.BigAutoField(primary_key=True)
    first_name = models.CharField('First Name', max_length=50)
    last_name = models.CharField('Last Name', max_length=50)
    email = models.EmailField('Email Address', unique=True)
    phone_number = models.CharField('Phone Number', max_length=20,unique=True)
    address = models.CharField('Address', max_length=200)
    city = models.CharField('City', max_length=50)
    state = models.CharField('State', max_length=50)
    zip_code = models.CharField('Zip Code', max_length=10)

    class Meta:
        verbose_name_plural = 'Customers'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
