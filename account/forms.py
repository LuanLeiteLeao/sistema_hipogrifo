from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import  forms
from .models import User
from django.forms import ModelForm, Textarea

class UserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = ('email',)


class UserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('email',)

class UserCreationForm(UserCreationForm):
	
  def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      self.fields['nome'].widget.attrs.update({'placeholder':'Nome'})
      self.fields['email'].widget.attrs.update({'placeholder':'Email'})
      self.fields['cpf'].widget.attrs.update({'placeholder':'CPF'})
      self.fields['password1'].widget.attrs.update({'placeholder':'Password'})
      self.fields['password2'].widget.attrs.update({'placeholder':'Confirme sua senha'})

  class Meta:
  	model = User
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

class EditeUserForm(UserCreationForm):
    """
    esta classe erda da classe UserCreationForm criada nesse aquivo,
    porem no seu metodo contrutor ele tirar aobrigatoriedade das senhas,
    possa ser que o usuário não queira editar a senha, como a senha n vem preechida
    e o campo n pode ser mandado vazio..... 
    """
    def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      self.fields['password1'].required = False
      self.fields['password2'].required = False 
      self.fields['password1'].widget.attrs.update({'style': 'display:none'});
      self.fields['password2'].widget.attrs.update({'style': 'display:none'});           