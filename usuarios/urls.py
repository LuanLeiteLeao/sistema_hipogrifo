from django.urls import path, include
from .views import *
from django.contrib.auth.views import logout_then_login

urlpatterns = [
    # path('logar_usuario', logar_usuario, name="logar_usuario"),
    path('cadastrar', cadastrar_usuario, name="cadastrar_usuarios"),
    path('',index, name="index_usuarios"),
    path('login',logar_usuario,name='login'),
    path('test',teste_de_login,name='teste_de_login'),
    path('redefinir_senha',redefinir_senha,name='redefinir_senha')
    # path('index', index, name="index"),
]