from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.decorators import login_required
from account.models import User
from django.shortcuts import get_object_or_404
from account.forms import UserCreationForm,EditeUserForm
from account.constantes import ADMINISTRADOR,ALUNO,PROFESSOR
from .niveis_de_usuario import has_user_permission
from account.uteis import gerar_senha


@login_required(login_url='/account/signin')
@has_user_permission(tipo_usuario_permitidos=[ADMINISTRADOR])
def listar_usuarios(request):
	all_users = User.objects.all()
	
	# return render(request,'base_administrador.html',{'all_users':all_users})
	return render(request,'administrador/listar_usuarios.html',{'all_users':all_users})

@login_required(login_url='/account/signin')
def excluir_usuario(request,id):
	user = User.objects.get(id=id)
	return render(request,'administrador/confirmar_exclusao.html',{'user':user})

@login_required(login_url='/account/signin')
def confirmar_exclusao(request,id):
	user = User.objects.get(id=id)
	user.delete()
	print("OIIIIIII")
	return redirect(listar_usuarios)	

@login_required(login_url='/account/signin')
def editar_usuario(request,id):
	user = get_object_or_404(User,id=id)
	
	if request.method == 'POST':
		form = EditeUserForm(request.POST, instance=user)
		# form = EditeUserForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('listar_usuarios')
		else:
			print(form.errors)	
	else:
		form = EditeUserForm(instance=user)

	return render(request,'administrador/editar_usuario.html',{'form':form})

@login_required(login_url='/account/signin')
@has_user_permission(tipo_usuario_permitidos=[ADMINISTRADOR])
def confirmar_resetar_senha(request,id):
	user = User.objects.get(id=id)
	return render(request,'administrador/confirmar_resetar_senha.html',{'user':user})

@login_required(login_url='/account/signin')
@has_user_permission(tipo_usuario_permitidos=[ADMINISTRADOR])
def resetar_senha(request,id):
	"""
	gera um senha aleatorio para o usuario e manda por email
	"""

	user = get_object_or_404(User,id=id)
	gerar_senha(user.email,user.cpf)

	return redirect(listar_usuarios)






