"""embrapaBee URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from bee.views import *
from usuarios.views import *
from django.contrib.auth import views as v

from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'usuarios', UserViewSet)
router.register(r'apicultores', ApicultorViewSet)
router.register(r'apiarios', ApiarioViewSet)
router.register(r'caixas_racionais', CaixaRacionalViewSet)
router.register(r'perdas', PerdaViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),

    path('index', index, name='index'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('apicultor/redefinir_senha',RedefinirSenhaView.as_view(), name='redefinir_senha'),
    path('registrar/', RegistrarUsuarioView.as_view(), name="registrar"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', v.LogoutView.as_view(template_name = 'login.html'), name="logout"),
    path('apicultor/apiarios/novo_apiario', RegistrarApiarioView.as_view(), name='novo_apiario'),
    path('apicultor/apiarios/<int:apiario_id>/excluir', deletar_apiario, name='excluir_apiario'),  
    path('apiarios/caixa/<int:apiario_id>', RegistrarCaixaRacionalView.as_view(), name='nova_caixa_racional'),
    path('apiarios/perda/<int:apiario_id>', RegistrarPerdaView.as_view(), name='nova_perda'),
    


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = router.urls + urlpatterns
