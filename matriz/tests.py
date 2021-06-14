from django.test import TestCase,Client
from matriz.models import Matriz
from django.utils import timezone
# Create your tests here.

class TestViewMatriz(TestCase):

	def setUp(self):
		self.client = Client()
		# matriz para fazer testes que reques uma matriz salva no banco de dados
		self.matriz_test = Matriz.objects.create(nome="Nome de Test",ano=timezone.now(),status=True,carga_horaria=100)

	def test_create_matriz(self):
		matriz = Matriz.objects.create(nome="Nome de Test",ano=timezone.now(),status=True,carga_horaria=100)
		self.assertTrue(isinstance(matriz,Matriz))
		matriz.delete()

	def test_form_crete_matriz(self):
		# testando cadastro de cliente pelo formulario 
		response = self.client.post("/matriz/cadastrar",{"nome":"Nome de Test","ano":"12/12/12","status":1,"carga_horaria":100})
		# casso tenha dado tudo certo o servidor reponde 200 
		self.assertEqual(response.status_code,200) 

	def test_listar_matriz(self):
		# testar se ha resposta da pagina de listar matriz
		response = self.client.get("/matriz/listar")
		self.assertEqual(response.status_code,200) 

	def test_confirmar_exclusao(self):
		response = self.client.get("/matriz/confirmar_exclusao/{}".format(self.matriz_test.id))
		self.assertEqual(response.status_code,200)

	def test_excluir_usuario(self):
		response = self.client.post("/matriz/excluir/{}".format(self.matriz_test.id))
		# 302 e usado para redirecinamento de pagina
		self.assertEqual(response.status_code,302)

	def test_editar_matriz_get(self):
		response = self.client.get("/matriz/editar/{}".format(self.matriz_test.id))
		self.assertEqual(response.status_code,200)

	def test_editar_matriz_post(self):
		response = self.client.post("/matriz/editar/{}".format(self.matriz_test.id),{"nome":"","ano":"12/12/12","status":1,"carga_horaria":100})
		self.assertEqual(response.status_code,200)