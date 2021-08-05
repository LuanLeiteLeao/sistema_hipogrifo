from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .forms import MatrizCreationForm
from .models import Matriz
from django.contrib.auth.decorators import login_required
from account.models import User
# Create your views here.

# administrador
def cadastrar_matriz(request):	
	form =  MatrizCreationForm()
	context = {'form':form}

	if request.method == 'POST':
		form = MatrizCreationForm(request.POST)

		if form.is_valid():
			form.save()
			context.update({'success':"salvo com sucesso"}) 
		else:
			context.update({'erros':form.errors}) 

	return render(request,'matriz/cadastrar_matriz.html',context)

# administrador
def listar_matriz(request):
	matriz = Matriz.objects.all()
	context = {"all_matriz":matriz}

	return render(request,"matriz/listar_matriz.html",context)

# administrador
def confirmar_exclusao_matriz(request,id):
	try:	
		matriz = Matriz.objects.get(id=id)
		return render(request,'matriz/confirmar_exclusao.html',{'matriz':matriz})
	except :
		# caso a matriz nao exista da page not foud
		return HttpResponse(status=404)	

# administrador
def excluir_matriz(request,id):
	
	matriz = Matriz.objects.get(id=id)
	matriz.delete()
	
	return render(listar_matriz)	

# administrador
def editar_matriz(request,id):
	matriz = get_object_or_404(Matriz,id=id)
	context = {}

	if request.method == "POST":
		
		form = MatrizCreationForm(request.POST,instance=matriz)

		if form.is_valid():
			form.save()
			return redirect(listar_matriz)

		else:
			print(form.errors)
	else:
		context.update({'form':MatrizCreationForm(instance=matriz)})
	
	return render(request,'matriz/cadastrar_matriz.html',context)
	
# aluno
@login_required(login_url='/account/signin')
def escolher_matriz_aluno(request):
	context = {}
	if request.user.matriz:
		return HttpResponse("já possui martiz cadastrada")
	if request.POST:
		value = request.POST.get('matriz')	
		user = get_object_or_404(User,id=request.user.id)
		matriz = get_object_or_404(Matriz,id=value)
		user.matriz=matriz
		user.save()
	
	matriz = Matriz.objects.all()
	context.update( {"all_matriz":matriz})
	
	return render(request,'matriz/escolher_matriz_aluno.html',context)