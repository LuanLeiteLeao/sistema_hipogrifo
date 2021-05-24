from django.urls import path
from .views import *
from django.contrib.auth.views import logout_then_login

urlpatterns = [
    path('',index, name="index_usuarios"),
    # ambas urls login e singin sao para realizar login 
    path('signin',signin,name='signin'),
    path('login',signin,name='login'),
    # ambas urls cadastrar e singup sao para realizar cadastro 
    path('signup',signup,name='signup'),
    path('cadastrar',signup,name='cadastrar'),
    path('test',teste_de_login,name='teste_de_login'),
    path('redefinir_senha',redefinir_senha,name='redefinir_senha')
]