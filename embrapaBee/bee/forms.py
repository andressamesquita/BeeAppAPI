from django import forms
from django.contrib.auth.models import User

class RegistrarApiarioForm(forms.Form):

    tipo = forms.CharField(required=True)
    qtd_colmeias = forms.IntegerField(required=True)
    localizacao = forms.CharField(required=True)

    def adiciona_erro(self, message):
        errors = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
        errors.append(message)

class RegistrarCaixaRacionalForm(forms.Form):

    identificador = forms.CharField(required=True)
    especie = forms.CharField(required=True)

    def adiciona_erro(self, message):
        errors = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
        errors.append(message)

