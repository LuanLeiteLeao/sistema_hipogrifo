from django.urls import path
from .views import *

urlpatterns = [
	path("cadastrar", cadastrar_matriz, name="cadastrar_matriz"),
	path("listar", listar_matriz, name="listar_matriz"),
	path("excluir/<id>", excluir_matriz, name="excluir_usuario"),
	path("confirmar_exclusao/<id>", confirmar_exclusao_matriz, name="confirmar_exclusao_matriz"),
	path("editar/<id>", editar_matriz, name="editar_matriz"),
]