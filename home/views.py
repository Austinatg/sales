from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout, login
from .forms import UserRegisterForm
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.contrib import messages
from .models import Sales

#Austin@2003
# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect('/login')
    return render(request, 'index.html')

def home_view(request):
    if request.user.is_authenticated:
        sales = Sales.objects.filter(user=request.user)
        return render(request, 'index.html', {'sales': sales})
    else:
        return redirect('login')

def loginuser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, "Invalid username or password.")
            return render(request, 'login.html', {'invalid_credentials': True}) 
            # Pass a context variable to indicate authentication error

    return render(request, 'login.html', {'invalid_credentials': False}) 

def logoutuser(request):
    logout(request)
    return redirect('/login')

# def register(request):
#     print(request.POST.get('username'))
#     if request.method == 'POST':
#         print("inside")
#         form = UserRegisterForm(request.POST)
#         password1 = request.POST.get('password1')
#         password2 = request.POST.get('password2')
#         print(password1)
#         print(password2)
#         if password1 != password2:
#             print("doesnt match")
#             messages.error(request, "Password doesn't match")
#         elif form.is_valid():
#             print("valid")
#             form.save()
#             username = form.cleaned_data.get('username')
#             email = form.cleaned_data.get('email')
#             ######################### mail system #################################### 
#             htmly = get_template('user/Email.html')
#             d = { 'username': username }
#             subject, from_email, to = 'welcome', 'your_email@gmail.com', email
#             html_content = htmly.render(d)
#             msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
#             msg.attach_alternative(html_content, "text/html")
#             msg.send()
#             ################################################################## 
#             messages.success(request, f'Your account has been created ! You are now able to log in')
#             return redirect('login')
#     else:
#         form = UserRegisterForm()
#     return render(request, 'register.html')#, {'form': form, 'title':'register here'})

def register(request):
    if request.method == 'POST':
        print("YES")
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            # return redirect('login')
        else:
            messages.error(request, "Didn't match the criteria check your email and password or the username is already taken")
    else:
        print("NO")
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

from .forms import SaleForm

def add_product(request):
    if request.method == 'POST':
        form = SaleForm(request.POST, request.FILES)
        if form.is_valid():
            sale = form.save(commit=False)
            sale.user = request.user
            sale.save()
            return redirect('home')  # Adjust this to your home URL name
    else:
        form = SaleForm()
    return render(request, 'add_product.html', {'form': form})

from django.views import View

class AddProductView(View):
    def get(self, request):
        form = SaleForm()
        return render(request, 'add_product.html', {'form': form})

    def post(self, request):
        form = SaleForm(request.POST, request.FILES)
        if form.is_valid():
            sale = form.save(commit=False)
            sale.user = request.user
            sale.save()
            return redirect('home')
        return render(request, 'add_product.html', {'form': form})
    


def streamlit_view(request):
    return render(request, 'streamlit_view.html')


from django.http import JsonResponse
from .models import Sales

def sales_data(request):
    sales = Sales.objects.all().values()
    return JsonResponse(list(sales), safe=False)


from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Sales

@login_required
def get_sales_data(request):
    user = request.user
    sales = Sales.objects.filter(user=user).values()
    sales_data = list(sales)  # Convert QuerySet to a list
    return JsonResponse(sales_data, safe=False)


from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@login_required
def get_current_username(request):
    username = request.user.username
    return Response({'username': username})

@login_required
def streamlit_app(request):
    return render(request, 'streamlit_view.html')