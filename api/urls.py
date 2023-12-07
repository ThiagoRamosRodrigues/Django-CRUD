from django.urls import path
from . import views
from .views import fazer_previsao
app_name = 'api'
urlpatterns = [
    path('', views.ApiOverview, name='home'),
    path('criarUsuario/', views.add_user, name='add-user'),
    path('listarUsuarios/', views.view_users, name='view_users'),
    path('atualizar/<int:pk>/', views.update_users, name='update-items'),
    path('usuario/<int:pk>/deletar/', views.delete_users, name='delete-users'),
    path('fazer_previsao/<int:id_dado>/', fazer_previsao, name='fazer_previsao'),
]
