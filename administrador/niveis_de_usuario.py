from django.contrib.auth.decorators import user_passes_test
from account.models import User

def has_user_permission(function=None,tipo_usuario_permitidos=None):
    def is_customer(u):
    	is_achei = False

    	try:
    		user = User.objects.get(id=u.id)	
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