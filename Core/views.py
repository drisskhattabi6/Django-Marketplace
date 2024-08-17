from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from Item.models import Category, Item


def index(request):
    items = Item.objects.filter(is_sold=False)[:12]
    categories = Category.objects.all()

    context = {
        'categories': categories,
        'products': items,
    }

    return render(request, 'core/index.html', context)


def loginPage(request):

    if request.user.is_authenticated:
        return redirect('core:index')
        # return redirect(f"{settings.LOGIN_URL}?next={request.path}")

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('core:index')  # Redirect to your desired page after login
        else:
            # Handle invalid login
            return render(request, 'authentication/login.html', {'error_message': 'invalid username or password!'})
        
    return render(request, 'authentication/login.html')


def registerPage(request):

    if request.user.is_authenticated:
        return redirect('index')

    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # user = form.save()
            user = User.objects.create_user(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password1'],
                email = request.POST['email'],
                first_name = request.POST['first_name'],
                last_name = request.POST['last_name']
            )

            login(request, user)

            return redirect('core:index')

    return render(request, 'authentication/register.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('core:index') 

