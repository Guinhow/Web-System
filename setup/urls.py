
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from main import views 



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('inicio/', views.restrita, name='Página Inicial'),
    path('formulario/', views.formulario, name='formulario'),  
    path('filtroAmostra/', views.consultar_dados, name='filtroAmostra'),
    path('resultados/', views.resultados, name='resultados'),
    path('filtroAresultados/', views.filtroAresultados, name='filtroAresultados'),
    path('laudos/', views.laudos, name='laudos'),
    path('saidaAmostra/', views.saidaAmostra, name='saidaAmostra'),
    path('filtrosaida/', views.filtrosaida, name='filtrosaida'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('filtrocadastro/', views.filtrocadastro, name='filtrocadastro'),
    path('estoque/', views.estoque, name='estoque'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('remover/<int:dado_id>/', views.remover_dado, name='remover_dado'),
]
if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()