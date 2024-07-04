# myapp/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User

class CustomUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    error_messages = {
        'password_mismatch': ("Las contraseñas no coinciden."),
        'password_too_short': ("La contraseña es demasiado corta."),
        'password_too_common': ("La contraseña es demasiado común."),
        'password_entirely_numeric': ("La contraseña no puede ser enteramente numérica."),
    }
    
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        
    def __init__(self, *args, **kwargs):
        super(CustomUserForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
