from django.core.management.utils import get_random_secret_key
from .models import User  
from emails import send_email

def gerar_senha(email,cpf):
	try:
		user = User.objects.get(email=email,cpf=cpf)
	except :
		return False

	senha_gerada = get_random_secret_key()
	user.set_password(senha_gerada)
	user.save()
	send_email.confirmacao_novo_cadastro_pessoa(user.nome,senha_gerada,'luanleiteraio@gmail.com')
	