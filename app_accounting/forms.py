
from django import forms 
from django.contrib.auth.forms import UserCreationForm 
from app_accounting.models import User 
from django.contrib.auth.forms import PasswordChangeForm 
from .models import MessagingModel, ConsultingModel, NewsletterModel  


class CustomUserCreationForm(UserCreationForm): 
    class Meta: 
        model = User 
        fields = ('username',)
        labels = { 
            'username': 'username', 
        } 


class MyPasswordChangeForm(PasswordChangeForm): 
    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs) 

        for field_name in ['old_password','new_password1','new_password2'] : 
            self.fields[field_name].widget = forms.PasswordInput() 


class MessagingForm(forms.ModelForm):  
    class Meta: 
        model = MessagingModel 
        fields = ('email', 'phone_number', 'your_comment') 


class ConsultingForm(forms.ModelForm): 
    class Meta: 
        model = ConsultingModel 
        fields = ('email', 'phone_number')   


class NewsletterForm(forms.ModelForm): 
    class Meta: 
        model = NewsletterModel 
        fields = ('email',)




