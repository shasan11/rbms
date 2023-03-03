from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager

from django.db import models
from branch.models import Branch
class CustomUser(AbstractUser):
    branch=models.ForeignKey(Branch,on_delete=models.CASCADE,verbose_name="Branch",related_name="restaurant_branch",null=True,blank=True)
    is_staff = models.BooleanField(default=True,editable=False)
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name='customuser_groups',
        related_query_name='customuser',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='customuser_user_permissions',
        related_query_name='customuser',
    )

    def __str__(self):
        if self.branch!=None:
            return self.username+"-"+str(self.branch)
        else:
            
            return str(self.first_name)+" "+str(self.last_name)
    
 
 
"""class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
         
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)
"""