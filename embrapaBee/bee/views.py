from django.shortcuts import render, redirect
from rest_framework import viewsets
from django.views.generic.base import View
from bee.serializers import *
from bee.models import *
from usuarios import views
from django.contrib.auth.decorators import login_required
from bee.forms import *
# Create your views here.

@login_required
def index(request):

    perfil_logado = get_usuario_logado(request)
    apiarios = Apiario.objects.filter(apicultor=perfil_logado.apicultor.id)
    
    
    contexto = {
        'perfil_logado': perfil_logado,
        'apiarios': apiarios,     
    }

    return render(request, 'index.html', contexto)


@login_required
def get_usuario_logado(request):	
	return request.user


class RegistrarApiarioView(View):
	template_name = 'registrarApiario.html'

	def get(self, request):
		return render (request, self.template_name)
	
	def post(self, request):
		form = RegistrarApiarioForm(request.POST)
		if form.is_valid ():
			dados_form = form.cleaned_data
			apiario = Apiario(apicultor = get_usuario_logado(request).apicultor, tipo = dados_form['tipo'], qtd_colmeias = dados_form['qtd_colmeias'], localizacao = dados_form['localizacao'])
			apiario.save()
			
			usuario_logado = get_usuario_logado(request)
			apiarios = Apiario.objects.filter(apicultor=usuario_logado.apicultor.id)

			contexto = {
				'perfil_logado': usuario_logado,
				'apiarios': apiarios
			}

			return render(request, 'index.html', contexto)

		return render(request, self.template_name, {'form':form})


class RegistrarCaixaRacionalView(View):
    template_name = 'registrarCaixaRacional.html'

    def get(self, request, apiario_id):
        apiario = Apiario.objects.get(id=apiario_id)

        contexto = {
            "apiario": apiario
        }

        return render (request, self.template_name, contexto)

    def post(self, request, apiario_id):
        form = RegistrarCaixaRacionalForm(request.POST)

        if form.is_valid():
            dados_form = form.cleaned_data
            apiario = Apiario.objects.get(id=apiario_id)
            caixa_racional = CaixaRacional(apiario=apiario, identificador = dados_form['identificador'], especie = dados_form['especie'])
            caixa_racional.save()

            caixas_racionais = CaixaRacional.objects.filter(apiario=apiario)
            apiario = Apiario.objects.get(id=apiario_id)

            contexto = {
                'caixas_racionais': caixas_racionais,
                'apiario': apiario
                }

            return render(request, 'caixaRacional.html', contexto)

        return render(request, self.template_name, {'form':form})

class RegistrarPerdaView(View):
    template_name = 'registrarPerda.html'

    def get(self, request, apiario_id):
        apiario = Apiario.objects.get(id=apiario_id)

        contexto = {
            "apiario": apiario
        }

        return render (request, self.template_name, contexto)

    def post(self, request, apiario_id):
        form = RegistrarPerdaForm(request.POST, request.FILES)

        if form.is_valid():
            dados_form = form.cleaned_data
            apiario = Apiario.objects.get(id=apiario_id)
            perda = Perda(apiario=apiario, tipo_perda = dados_form['tipo_perda'], qtd_colmeias_perdidas = dados_form['qtd_colmeias_perdidas'], 
                            data_registro_perda = dados_form['data_registro_perda'], especie_perdida = dados_form['especie_perdida'], foto_perda = dados_form['foto_perda'])
            perda.save()

            perdas = Perda.objects.filter(apiario=apiario)
            apiario = Apiario.objects.get(id=apiario_id)

            contexto = {
                'perdas': perdas,
                'apiario': apiario
                }

            return render(request, 'perdasRegistradas.html', contexto)

        return render(request, self.template_name, {'form':form})


@login_required
def deletar_apiario(request, apiario_id):
	apiario = Apiario.objects.get(id=apiario_id)
	apiario.excluir_apiario()
	
	perfil_logado = get_usuario_logado(request)
	apiarios = Apiario.objects.filter(apicultor=perfil_logado.apicultor.id)

	contexto = {
		'perfil_logado': perfil_logado,
		'apiarios':apiarios
	}

	return render(request, 'index.html', contexto)

def base_layout(request):
	template='/bee/templates/base.html'
	return render(request,template)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class ApicultorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Apicultor.objects.all()
    serializer_class = ApicultorSerializer

class ApiarioViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Apiario.objects.all()
    serializer_class = ApiarioSerializer

class CaixaRacionalViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = CaixaRacional.objects.all()
    serializer_class = CaixaRacionalSerializer

class PerdaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Perda.objects.all()
    serializer_class = PerdaSerializer
