from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from usuarios.models import CustomUser
from django.shortcuts import get_object_or_404
from usuarios.forms import UserCreationForm
from usuarios.constantes import ADMINISTRADOR,ALUNO,PROFESSOR
from .niveis_de_usuario import has_user_permission


@login_required(login_url='/usuarios/login')
@has_user_permission(tipo_usuario_permitidos=[ADMINISTRADOR])
def listar_usuarios(request):
	all_users = CustomUser.objects.all()
	return render(request,'administrador/listar_usuarios.html',{'all_users':all_users})

@login_required(login_url='/usuarios/login')
def excluir_usuario(request,id):
	user = CustomUser.objects.get(id=id)
	return render(request,'administrador/confirmar_exclusao.html',{'user':user})

@login_required(login_url='/usuarios/login')
def confirmar_exclusao(request,id):
	user = CustomUser.objects.get(id=id)
	user.delete()
	return redirect(listar_usuarios)	

@login_required(login_url='/usuarios/login')
def editar_usuario(request,id):
	user = get_object_or_404(CustomUser,id=id)
	form = UserCreationForm(instance=user)

	return render(request,'administrador/editar_usuario.html',{'form':form})


