from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from accounts.forms import RegistrationForm

# Create your views here.
def signup_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = request.POST.get('email')
            password = request.POST.get('pass')
            account = authenticate(email=email, password=password)
            login(request, account)
            return redirect('dashboard')
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'accounts/signup.html', context)

def login_view(request):
    return render(request, 'accounts/login.html', {})

def logout_view(request):
    logout(request)
    return redirect('dashboard')
