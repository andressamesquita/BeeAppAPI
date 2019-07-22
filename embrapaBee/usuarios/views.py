from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordChangeForm
from django.views.generic.base import View
from usuarios.forms import *
from django.contrib.auth import authenticate, login
from django.db import transaction
from bee.models import Apicultor

class LoginView(View):
    template_name = 'login.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
	
        if user is not None:
            login(request, user)
            return redirect('index')

        return render(request, self.template_name, {"form":form})

class RegistrarUsuarioView(View):
	template_name = 'registrar.html'

	def get(self, request):
		return render (request, self.template_name)
	

	def post(self, request):
		form = RegistrarUsuarioForm (request.POST)
		if form.is_valid ():
			dados_form = form.cleaned_data
			usuario = User.objects.create_user (username = dados_form['nome'], email = dados_form['email'], password = dados_form['senha'])
			perfil = Apicultor(nome=dados_form['nome'], qtd_apiarios = dados_form['qtd_apiarios'], tipo_criador = dados_form['tipo_criador'], usuario = usuario)
			perfil.save()
			
			return redirect('login')

		return render(request, self.template_name, {'form':form})

class RedefinirSenhaView(View):
	template_name = 'redefinir_senha.html'

	def get(self, request):
		form = RedefinirSenhaForm()
		return render(request, self.template_name, {'form': form})
	
	def post(self, request):
		form = RedefinirSenhaForm(request.POST)
		usuario_logado = User.objects.get(id=request.user.id)
		if form.is_valid():
			dados_form = form.cleaned_data
			if usuario_logado.check_password(dados_form['senha_atual']):
				if dados_form['nova_senha'] == dados_form['confirmacao_nova_senha']:
					usuario_logado.set_password(dados_form['nova_senha'])
					usuario_logado.save()
					return redirect('index')
		
		return render(request, self.template_name, {'form':form})