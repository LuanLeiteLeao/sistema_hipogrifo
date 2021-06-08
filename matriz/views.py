from django.shortcuts import render,HttpResponse,redirect
from .forms import MatrizCreationForm
from .models import Matriz
# Create your views here.

# administrador
def cadastrar_matriz(request):	
	form =  MatrizCreationForm()
	context = {'form':form}

	if request.method == 'POST':
		form = MatrizCreationForm(request.POST)

		if form.is_valid():
			form.save()
		else:
			context.update({'erros':form.errors}) 

	return render(request,'matriz/cadastrar_matriz.html',context)

# administrador
def listar_matriz(request):
	matriz = Matriz.objects.all()
	context = {"all_matriz":matriz}

	return render(request,"matriz/listar_matriz.html",context)

def confirmar_exclusao(request,id):
	
	try:	
		matriz = Matriz.objects.get(id=id)
		return render(request,'matriz/confirmar_exclusao.html',{'matriz':matriz})
	except :
		# caso a matriz nao exista da page not foud
		return HttpResponse(status=404)	

def excluir_usuario(request,id):
	
	if request.method == "POST":
		matriz = Matriz.objects.get(id=id)
		matriz.delete()

	return redirect(listar_matriz)	
