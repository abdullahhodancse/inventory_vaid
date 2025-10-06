from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from app_inv.models.catagory import catagory


# Create your models here.
class usermanger(BaseUserManager):
    def create_user(self,email,password=None,**extra_fields):
        if not email:
            raise ValueError("You must give email address")
        email=self.normalize_email(email)    #email k normal text e convert korbe,,,,
        user=self.model(email=email,**extra_fields) #obkect create kora hoyeche,ai kahne shudu email neya hoice,,,password neya hoyni karon ai kahne nile plain text thakbe kinto passwors sob somoi hash kora lage
        user.set_password(password) # now hash tha passs
        user.save(using=self.db) # sava it in database
        return user
    

    def create_superuser(self,email,password,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)


        if extra_fields.get('is_staff') is not True:
            raise ValueError('superuser must be in true')
                   
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Super user must be is_superuser=true')
        
        return self.create_user(email,password,**extra_fields)
    

class User(AbstractBaseUser,PermissionsMixin):
    email=models.EmailField(unique=True)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    
    catagory=models.ManyToManyField(catagory,null=True, blank=True)

    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)

    objects=usermanger()


    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]


    def __str__(self):
        return self.email
