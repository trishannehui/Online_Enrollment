from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import RegistrationForm



#Registration Views
def register_user(request):
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Account Created Successfully')
            return redirect('login_user')
        
        else:
            messages.error(request,'Please correct the errors below.')
    else:
        form = RegistrationForm()
    return render(request,'accounts/register.html',{'form':form})

#Login Views

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {username}!')
                return redirect('dashboard')
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request, 'Invalid input')
        return render(request, 'accounts/login.html', {'form': form})

    else:
        form = AuthenticationForm()
        return render(request, 'accounts/login.html', {'form': form})
                     
#Logout Views
def logout_user(request):
    logout(request)
    messages.info(request,'Your have been logged out')
    return redirect('login_user')

#Dashboard views

def dashboard(request):
    return render(request,'accounts/dashboard.html')



