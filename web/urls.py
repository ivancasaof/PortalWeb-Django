from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index' ),
    path('comunicados/', views.comunicados, name='comunicados' ),
    path('comunicados/<int:noticia_id>', views.comunicados_ativo, name='comunicados_ativo' ),
    path('eventos/', views.eventos, name='eventos' ),
    path('eventos/<int:evento_id>', views.eventos_ativo, name='eventos_ativo' ),
    path('rh_comunicados/', views.rh_comunicados, name='rh_comunicados' ),
    path('rh_comunicados/<int:rh_comunicados_id>', views.rh_comunicados_ativo, name='rh_comunicados_ativo' ),
    path('index/<int:noticias_id>', views.noticias_geral, name='noticias_geral' ),
    path('empresa/', views.empresa, name='empresa' ),
]