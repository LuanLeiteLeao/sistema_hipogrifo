from django.urls import path
from .views import *

urlpatterns = [
	path("cadastrar", cadastrar_matriz, name="cadastrar_matriz"),
	path("listar", listar_matriz, name="listar_matriz"),
	path("excluir_usuario/<id>", excluir_usuario, name="excluir_usuario"),
	path("confirmar_exclusao/<id>", confirmar_exclusao, name="confirmar_exclusao"),
]