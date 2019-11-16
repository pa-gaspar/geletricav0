from django.urls import path
from . import views



from django.contrib import admin
from django.urls import path
from bancoDeDados.views import paginaSimples,bancoDeDados, areaVisualisacao, localVisualisacao, adicionarCarga



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', paginaSimples.as_view(),name='paginainicial'),
    path('sobre/', paginaSimples.as_view(template_name='sobre.html'),name='sobre'),
    path('bancodados/', bancoDeDados.as_view(template_name='bancoDeDados.html'),name='bancodedados'),
    path('bancodados/<int:id1>/',areaVisualisacao.as_view(template_name='area.html'),name='area'),
    path('bancodados/<int:id1>/<int:id2>/',localVisualisacao.as_view(template_name='local.html'),name='local'),
    #path('addcargalocal<int:id1>/', adicionarCarga.as_view(),name='adicionarcarga'),
    path('addcarga/', adicionarCarga,name='adicionarcarga'),
]