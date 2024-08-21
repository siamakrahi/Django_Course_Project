from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.db import models

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_("username"), max_length=150, unique=True) 
    first_name = models.CharField(_("firstname"), max_length=150)
    last_name = models.CharField(_("lastname"), max_length=150)
    email = models.EmailField(_("email"), unique=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True)
    about = models.TextField(blank=True)
    USERNAME_FIELD = 'username' 
    REQUIRED_FIELDS = ['email']
    is_staff = models.BooleanField(default=False) 
    is_active = models.BooleanField(default=True)
    

    def __str__(self):
        return self.get_full_name()

class ContactModel(models.Model): 
    email = models.EmailField() 
    phone_number = models.CharField(max_length=20) 
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contact_info') 
    def __str__(self): 
        return f"{self.user.username} - {self.email}"
    

class MessagingModel(ContactModel): 
    your_comment = models.TextField() 
    def __str__(self): 
        return f"{self.user.username} - {self.email}" 
  
class ConsultingModel(ContactModel): 
    pass 

class NewsletterModel(models.Model): 
    email = models.EmailField(unique=True) 
    def __str__(self): 
        return self.email 
