from django.shortcuts import render, redirect,HttpResponse
from .forms import UserCreationForm,LoginForm,RedefinirSenhaForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import login
from .uteis import gerar_senha ,get_usuario_logado
from .constantes import *

def signin(request):
    context = {}
    context.update({'form_usuario':UserCreationForm()})
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        usuario = authenticate(request, email=email, password=password)
        if usuario is not None:
            print("eu entrei aqui")
            login(request, usuario)
            user = get_usuario_logado(usuario.id)  

            if usuario.tipo == ADMINISTRADOR[0]:
                return redirect('/administrador/')

            elif usuario.tipo == ALUNO[0]:
                return render(request,'usuarios/aluno.html')

            elif usuario.tipo == PROFESSOR[0]:
                return render(request,'usuarios/professor.html')

            # return redirect('teste_de_login')
        else:
             context.update({'erros':['Campo Usuário ou Senha: Inválido.']})
    return render(request,'account/login_novo_usuario.html',context)

def signup(request):
    if request.method == "POST":
        form_usuario = UserCreationForm(request.POST)
        if form_usuario.is_valid():
            form_usuario.save()
            return redirect('signin')
    else:
        form_usuario = UserCreationForm()
    return render(request, 'account/login_novo_usuario.html', {'form_usuario': form_usuario})

def redefinir_senha(request):
	if request.method == "POST":
		form_redefinir_senha = RedefinirSenhaForm(request.POST)
		if form_redefinir_senha.is_valid():
			#removendo - e . da mascara do cpf 000.000.000-00 
			cpf = request.POST['cpf'].replace('.','').replace('-','')
			email = request.POST['email']
			gerar_senha(email,cpf)
	return render(request,'usuarios/redefinir_senha.html', {'form_redefinir_senha':RedefinirSenhaForm()})

