from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import MyUser  # Asegúrate de importar tu modelo personalizado

class MyUserLoginForm(AuthenticationForm):
    class Meta:
        model = MyUser  # Especifica tu modelo personalizado
        fields = ['username', 'password']  # Campos para el inicio de sesión
