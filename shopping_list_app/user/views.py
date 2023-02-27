from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def index(request):
    return render(request, 'user/index.html')

def about(request):
    return render(request, 'user/about.html')


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, ("There was an error logging in...Try again"))
            return redirect('login')
    else:
        form = AuthenticationForm()
    return render(request, 'authenticate/login.html', {'form': form})

def logout_user(request):
    logout(request)
    messages.success(request, ("You were logged out!"))
    return redirect('home')







def sign_up(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # email = form.cleaned_data['email']
            # password = form.cleaned_data['password1']
            # user - authenticate() +login
            messages.success(request, ("Registration successful!"))
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'authenticate/sign_up.html', {'form': form})
