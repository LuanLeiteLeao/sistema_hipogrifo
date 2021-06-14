from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
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

def confirmar_exclusao_matriz(request,id):
	
	try:	
		matriz = Matriz.objects.get(id=id)
		return render(request,'matriz/confirmar_exclusao.html',{'matriz':matriz})
	except :
		# caso a matriz nao exista da page not foud
		return HttpResponse(status=404)	

def excluir_matriz(request,id):
	
	if request.method == "POST":
		matriz = Matriz.objects.get(id=id)
		matriz.delete()

	return redirect(listar_matriz)	

def editar_matriz(request,id):
	matriz = get_object_or_404(Matriz,id=id)

	if request.method == "POST":
		
		form = MatrizCreationForm(request.POST,instance=matriz)

		if form.is_valid():
			form.save()
			return render(listar_matriz)

		else:
			print(form.errors)

	
	return HttpResponse("oi")
	
