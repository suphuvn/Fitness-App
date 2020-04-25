from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from accounts.forms import RegistrationForm

def signup_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)

            if user:
                login(request, user)
                return redirect('/')
            else:
                return redirect('/accounts/login')
    else:
        form = RegistrationForm()

    return render(request, 'registration/signup.html', {'form': form})