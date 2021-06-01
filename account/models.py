from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from .managers import UserManager
from .constantes import TIPO_USUARIO_CHOICES

class User(AbstractBaseUser, PermissionsMixin):
    # determina se o usuario pode o nao acessar o django admin
    is_staff = models.BooleanField(default=False)
    # status do usuario ativo/desativo
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    email = models.EmailField(_('email address'), unique=True)
    nome = models.CharField("Nome", max_length=100, blank=False, null=True)
    cpf = models.CharField("CPF",max_length=11, blank=False, null=True, unique=True)
    tipo = models.IntegerField("Tipo de Usuário",choices=TIPO_USUARIO_CHOICES, blank=False, null=True)
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_tipo():
        return TIPO_USUARIO_CHOICES[self.tipo][1]