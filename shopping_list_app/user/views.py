from django.shortcuts import redirect, render, get_object_or_404, get_list_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from .models import Shopping_list, Product
from django.db.models import Sum
from .forms import *


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
    # shopping_list = get_list_or_404(Shopping_list, user_id = user_id)
    shopping_lists = user.shopping_list_set.all()
    # total = sum(position.price for position in shopping_list)
    # for position in shopping_list:
    #     total+=position.price
    context = {'shopping_lists': shopping_lists, 'username': username}
    return render(request, 'user/personal_area.html', context)

def create_list(request):
    if request.method == "POST":
        form = CreateShoppingListForm(request.POST)
        if form.is_valid():
            user = request.user
            # print(form.cleaned_data)
            try:
                Shopping_list.objects.create(label=form.cleaned_data['label'], user_id=user.id)
                return redirect('personal_area', user_id = user.id)
            except:
                form.add_error(None, 'Creation list error') 
            
    else:
        form = CreateShoppingListForm()
    return render(request, 'user/create_list.html', {'form': form})

def delete_list(request, list_id):
    try: 
        shopping_list = Shopping_list.objects.get(id = list_id)
        shopping_list.delete()
        return redirect('personal_area', user_id = request.user.id)
    except Shopping_list.DoesNotExist:
         messages.success(request, ("Shopping list not found"))


def manage_list(request, list_id):
    current_list = Shopping_list.objects.get(id = list_id)
    if request.method == "POST":
        form = CreateProductForm(request.POST)
        if form.is_valid():
            try:
               
                new_product = Product.objects.create(**form.cleaned_data)
                current_list.products.add(new_product)
                
                return redirect('manage_list', list_id = list_id)
            except:
                form.add_error(None, 'Creation product error')
        
    else:        
        form = CreateProductForm()
    products = current_list.products.all()
    total_price = sum(product.price for product in products)
    return render(request, 'user/manage_list.html', {'form': form, 'list_id': list_id, 'products': products, 'total_price': total_price})