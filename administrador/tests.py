from django.test import TestCase,Client
from account.models import User
from account.constantes import ADMINISTRADOR
from django.contrib.auth import login
# Create your tests here.

class TesteViewsAdministrador(TestCase):
	def setUp(self):
		self.client = Client()
		self.user  = User(email = "a@a.com",nome = "l",tipo = 1)
		self.user.set_password("123")
		
		self.user.save()



	def test_listar_usuarios(self):
		# print(self.user.tipo)
		# a = self.client.login()
		self.a = self.client.login(email = "a@a.com", password='123')
		
		response = self.a.get("/administrador")
		self.assertTrue(self.user.tipo in ADMINISTRADOR)
		self.assertEqual(response.status_code,200)
		print(response)
		