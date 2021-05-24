from django.shortcuts import render, redirect,HttpResponse
from .forms import UserCreationForm,LoginForm,RedefinirSenhaForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import login
from .uteis import gerar_senha  

# account ------------------- 

def signin(request):
    context = {}
    context.update({'form_usuario':UserCreationForm()})
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        usuario = authenticate(request, email=email, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('teste_de_login')
        else:
             context.update({'erros':['Campo Usuário ou Senha: Inválido.']})
    return render(request,'account/login_novo_usuario.html',context)

def signup(request):
    if request.method == "POST":
        form_usuario = UserCreationForm(request.POST)
        if form_usuario.is_valid():
            form_usuario.save()
            return redirect('index')
    else:
        form_usuario = UserCreationForm()
    return render(request, 'account/login_novo_usuario.html', {'form_usuario': form_usuario})
    # return render(request,'account/login_novo_usuario.html')
# account -------------------

# def cadastrar_usuario(request):
#     if request.method == "POST":
#         form_usuario = UserCreationForm(request.POST)
#         if form_usuario.is_valid():
#             form_usuario.save()
#             return redirect('index')
#     else:
#         form_usuario = UserCreationForm()
#     return render(request, 'usuarios/cadastro.html', {'form_usuario': form_usuario})

# def logar_usuario(request):
#     if request.method == "POST":
#         email = request.POST["email"]
#         password = request.POST["password"]
#         usuario = authenticate(request, email=email, password=password)
#         if usuario is not None:
#             login(request, usuario)
#             return redirect('teste_de_login')
#         else:
#             form_login = LoginForm()
#     else:
#         form_login = LoginForm()
#     return render(request, 'usuarios/login.html', {'form_login': form_login})

def redefinir_senha(request):
	if request.method == "POST":
		form_redefinir_senha = RedefinirSenhaForm(request.POST)
		if form_redefinir_senha.is_valid():
			#removendo - e . da mascara do cpf 000.000.000-00 
			cpf = request.POST['cpf'].replace('.','').replace('-','')
			email = request.POST['email']
			print('cpf ----->  {}'.format(cpf))	
			print('email ----->  {}'.format(email))
			print(gerar_senha(email,cpf))
	return render(request,'usuarios/redefinir_senha.html', {'form_redefinir_senha':RedefinirSenhaForm()})


def index(request):
	return render(request, 'usuarios/index.html')

@login_required(login_url='/usuarios/login')
def teste_de_login(request):
	return render(request,"usuarios/teste.html")	
