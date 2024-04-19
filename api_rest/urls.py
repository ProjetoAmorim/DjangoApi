# api_rest/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.user_list, name='user-list'),    # Rota para listar e criar usuários
    path('users/<str:nickname>/', views.user_detail, name='user-detail'),  # Rota para detalhes, atualização e exclusão de usuário
]
