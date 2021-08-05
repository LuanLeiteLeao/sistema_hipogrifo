from django.urls import path
from .views import *

urlpatterns = [
	path('',listar_usuarios,name='listar_usuarios' ),
	# parece q tem alguma url com esse nome
	path('excluir/<id>',excluir_usuario,name='excluir__usuario'),
	path('confirmar_exclusao/<id>',confirmar_exclusao,name='confirmar_exclusao'),
	path('editar/<id>',editar_usuario,name='editar_usuario'),
	path('confirmar_resetar_senha/<id>',confirmar_resetar_senha ,name='confirmar_resetar_senha'),
	path('resetar_senha/<id>',resetar_senha ,name='resetar_senha'),

]

