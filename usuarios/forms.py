from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import  forms
from .models import CustomUser
from django.forms import ModelForm, Textarea

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email',)

class UserCreationForm(UserCreationForm):
	
  def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      self.fields['nome'].widget.attrs.update({'placeholder':'Nome'})
      self.fields['email'].widget.attrs.update({'placeholder':'Email'})
      self.fields['cpf'].widget.attrs.update({'placeholder':'CPF'})
      # self.fields['password1'].widget.attrs.update({'placeholder':'Password'})        
      # self.fields['password2'].widget.attrs.update({'placeholder':'Confirme sua senha'})

  class Meta:
  	model = CustomUser
  	fields = ['email','nome','cpf','tipo']
    # widgets = {'cpf': forms.TextInput(attrs={'data-mask':"000-000-0000"})}
  	widgets = {
            'cpf': forms.TextInput(attrs={'data-mask':"000.000.000-00"}),
        }

class LoginForm(forms.Form):
  email = forms.EmailField(label='Email',required=True)
  password = forms.CharField(widget=forms.PasswordInput())

class RedefinirSenhaForm(forms.Form):
  email = forms.EmailField(label='Email',required=True)
  cpf = forms.CharField(label="CPF",widget=forms.TextInput( attrs={'data-mask':'000.000.000-00'}))