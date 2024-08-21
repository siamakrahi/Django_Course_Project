from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate    
from django.contrib.auth.forms import AuthenticationForm    
from django.contrib.auth.decorators import login_required    
from django.contrib.auth import logout    
from django.contrib import messages    
from .forms import NewsletterForm, ConsultingForm, MessagingForm, CustomUserCreationForm    
from .models import NewsletterModel, ConsultingModel, MessagingModel, User   
 
def about(request):   
    return render(request, 'about.html')   
 
def blog(request):   
    return render(request, 'blog.html')   
 
def contact(request):   
    return render(request, 'contact.html')   
 
def home(request):   
    return render(request, 'home.html')   
 
def service(request):   
    return render(request, 'service.html')   
 
def team(request):   
    return render(request, 'team.html')   


def login_view(request):    
    if request.method == 'POST':    
        form = AuthenticationForm(request, data=request.POST)    
        if form.is_valid():    
            username = form.cleaned_data.get('username')    
            password = form.cleaned_data.get('password')    
            user = authenticate(username=username, password=password)    
            if user is not None:    
                login(request, user)    
                return redirect('home')    
            else:    
                messages.error(request, "Invalid login credentials. Please check your details.")    
 
        else:    
            messages.error(request, "Invalid login form. Please check your details.")    
    else:    
        form = AuthenticationForm()    
    return render(request, 'login.html', {'form': form})  

def signup_view(request):    
    if request.method == 'POST':    
        form = CustomUserCreationForm(request.POST)     
        if form.is_valid():    
            form.save()    
            username = form.cleaned_data.get('username')    
            # نیازی به تایید مجدد رمز عبور نیست.   
            # password = form.cleaned_data.get('password1')   
            user = User.objects.get(username=username)   
            login(request, user)   
            messages.success(request, "Account created successfully!")   
            return redirect('home')   
        else:   
            messages.error(request, "Invalid signup form. Please check your details.")    
 
    else:    
        form = CustomUserCreationForm()    
    return render(request, 'signup.html', {'form': form})

def logout_view(request):   
    if request.method == "POST":   
        logout(request)   
        return redirect('home')   
    else:   
        return redirect('home')
    
@login_required    
def Newsletter_view(request):    
    if request.method == 'POST':    
        form = NewsletterForm(request.POST)    
        if form.is_valid():    
            email = form.cleaned_data.get('email')    
            newsletter = NewsletterModel(email=email)    
            newsletter.save()    
            messages.success(request, "ایمیل شما با موفقیت در لیست دریافت خبرنامه ثبت شد.")   
            return redirect('home')   
        else:    
            messages.error(request, "خطا در ثبت ایمیل. لطفا مجددا تلاش کنید.")    
            return render(request, 'contact.html', {'form': form})    
    else:    
        form = NewsletterForm()    
        return render(request, 'contact.html', {'form': form}) 

@login_required   
def Consulting_view(request):   
    if request.method == 'POST':   
        form = ConsultingForm(request.POST)   
        if form.is_valid():   
            form.save()   
            messages.success(request, "اطلاعات شما با موفقیت ثبت شد.")   
            return redirect('home')   
        else:   
            messages.error(request, "خطا در ثبت اطلاعات. لطفا مجددا تلاش کنید.")   
            return render(request, 'contact.html', {'form': form})   
    else:   
        form = ConsultingForm()   
        return render(request, 'contact.html', {'form': form})

@login_required   
def Messaging_view(request):   
    if request.method == 'POST':   
        form = MessagingForm(request.POST)   
        if form.is_valid():   
            form.save()   
            messages.success(request, "پیغام شما با موفقیت ثبت شد.")   
            return redirect('home')   
        else:   
            messages.error(request, "خطا در ثبت پیغام. لطفا مجددا تلاش کنید.")   
            return render(request, 'contact.html', {'form': form})   
    else:   
        form = MessagingForm()   
        return render(request, 'contact.html', {'form': form})