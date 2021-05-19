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
	class Meta:
		model = CustomUser
		fields = ['email','nome','cpf','tipo']
		# widgets = {
  #           'nome': Textarea(attrs={'cols': 80, 'rows': 20}),
  #       }

class LoginForm(forms.Form):
  email = forms.EmailField(label='Email',required=True)
  password = forms.CharField(widget=forms.PasswordInput())

class RedefinirSenhaForm(forms.Form):
  email = forms.EmailField(label='Email',required=True)
  cpf = forms.CharField(label="CPF",widget=forms.TextInput( attrs={'data-mask':'000.000.000-00'}))