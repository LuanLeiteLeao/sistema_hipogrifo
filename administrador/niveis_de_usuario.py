from django.contrib.auth.decorators import user_passes_test
from usuarios.models import CustomUser

def has_user_permission(function=None,tipo_usuario_permitidos=None):
    def is_customer(u):
    	is_achei = False

    	try:
    		user = CustomUser.objects.get(id=u.id)	
    	except :
    		print("ERRO DE EXEÇÃO: Usuário com ID {} não existe".format(u.id))	
    		raise Exception("ERRO DE BUSCA: Usuário com ID {} não existe".format(u.id))

    	for validos in tipo_usuario_permitidos:
    		if user.tipo in validos:
    			is_achei = True

    	return is_achei		

    actual_decorator = user_passes_test(is_customer)
    if function:
        return actual_decorator(function)
    else:
        return actual_decorator