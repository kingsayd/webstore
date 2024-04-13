from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.

class MyAccountManager(BaseUserManager):

  # first function create a user 
  def create_user(self, first_name, last_name ,username, email, password=None):
      if not email:
          raise ValueError('user must have email address') 
      if not username:
          raise ValueError('user must have an user name ')

      user = self.model(
          email = self.normalize_email(email),
          username = username,
          first_name = first_name,
          last_name = last_name,
      ) 

      user.set_password(password)
      user.save(using=self._db)
      return user
  def create_superuser(self, first_name, last_name, email, username, password):
      user = self.create_user(
          email= self.normalize_email(email),
          username= username,
          password= password,
          first_name= first_name,
          last_name= last_name,

      )
      user.is_admin = True
      user.is_active = True
      user.is_staff = True
      user.is_superadmin = True
      user.save(using=self._db)
      return user 





class Account(AbstractBaseUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username  = models.CharField(max_length=50,unique=True)
    email     = models.EmailField(max_length=100,unique=True)
    phone_number =models.CharField(max_length=50)

    # we have to mention some require field  is mandatory
    date_joined = models.DateTimeField(auto_now=True)
    last_login = models.DateTimeField(auto_now=True)
    is_admin   = models.BooleanField(default=False)
    is_staff   = models.BooleanField(default=False)
    is_active   = models.BooleanField(default=False)
    is_superadmin   = models.BooleanField(default=False)
# we have to set the login field we want to login with email address 
    USERNAME_FIELD = 'email'         # when we set this field we able to login with email address 
    REQUIRED_FIELDS =['username', 'first_name', 'last_name']

    objects = MyAccountManager()

    def __str__(self):
        return self.email             # this meens when return the account opject it should be return email address
    
    # we defin some mandatory method 

    def has_perm (self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, add_label):
        return True

   #we will make user model for supper user  
