from django.urls import path
from .views import *

urlpatterns = [
	path('',listar_usuarios,name='listar_usuarios' ),
	path('excluir/<id>',excluir_usuario,name='excluir_usuario'),
	path('confirmar_exclusao/<id>',confirmar_exclusao,name='confirmar_exclusao'),
	path('editar/<id>',editar_usuario,name='editar_usuario'),
]