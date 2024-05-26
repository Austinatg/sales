# from django import forms
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm

# class UserRegisterForm(UserCreationForm):
# 	email = forms.EmailField()
# 	user_name = forms.CharField(max_length = 20)
# 	class Meta:
# 		model = User
# 		fields = ['username', 'email', 'password1', 'password2']

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


from .models import Sales

class SaleForm(forms.ModelForm):
    class Meta:
        model = Sales
        fields = ['product', 'quantity', 'customer_name', 'receipt_img']
