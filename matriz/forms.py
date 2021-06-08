from django import forms
from .models import Matriz


class MatrizCreationForm(forms.ModelForm):
	class Meta:
		model = Matriz
		fields = ['nome','ano','status','carga_horaria']
		widgets =  {'ano':forms.DateInput(attrs={'type': 'date',})}