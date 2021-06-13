from django import forms
from .models import RegisterModel,ContactModel
class RegisterForm(forms.ModelForm):
   class Meta:
       model=RegisterModel
       fields='__all__'
class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = '__all__'
