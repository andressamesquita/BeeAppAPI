from django import forms
from django.contrib.auth.models import User


class RegistrarUsuarioForm(forms.Form):
	nome = forms.CharField(required=True)
	email = forms.EmailField(required=True)
	senha = forms.CharField(required=True)
	qtd_apiarios = forms.IntegerField()
	tipo_criador = forms.CharField(required=True)

	def adiciona_erro(self, message):
			errors = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
			errors.append(message)



class RedefinirSenhaForm(forms.Form):
	senha_atual = forms.CharField(required=True)
	nova_senha = forms.CharField(required=True)
	confirmacao_nova_senha = forms.CharField(required=True)

	def adiciona_erro(self, message):
		errors = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
		errors.append(message)


class LoginForm(forms.Form):
	username = forms.CharField(required=True)
	senha = forms.CharField(required=True)

	def adiciona_erro(self, message):
		errors = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
		errors.append(message)
    