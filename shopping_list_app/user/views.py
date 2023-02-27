from django.shortcuts import redirect, render, get_object_or_404, get_list_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from .models import Shopping_list


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
            user = request.user
            return redirect('personal_area', user_id = user.id)
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


def personal_area(request, user_id):
    user = get_object_or_404(get_user_model(), pk=user_id)
    username = user.get_username()
    shopping_list = get_list_or_404(Shopping_list, user_id = user_id)
    total = 0
    for position in shopping_list:
        total+=position.price
    return render(request, 'user/personal_area.html', {'shopping_list': shopping_list, 'username': username, 'total': total})