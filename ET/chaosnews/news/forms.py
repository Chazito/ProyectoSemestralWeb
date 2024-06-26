# myapp/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User

class CustomUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        
    def __init__(self, *args, **kwargs):
        super(CustomUserForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
