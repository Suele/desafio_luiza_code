from os import name
from django.urls.conf import include
from .views import CadastrarProduto, AtualizarProduto
from django.urls import path
from django.contrib.auth.decorators import login_required, permission_required

from.import views


urlpatterns = [
    
    path('', views.index, name='luMarketplace-index'),

    path('cadastrar-prod/', CadastrarProduto.as_view(),name='luMarketplace-cadastro'),

    path('atualizar-prod/', AtualizarProduto.as_view(),name='luMarketplace-atualizar'),    

    path('luMarketplace_deletar/<id_prod>', views.luMarketplace_deletar, name='luMarketplace-deletar'),
    
    path('luMarketplace_inativar/<id_prod>', views.luMarketplace_inativar, name='luMarketplace-inativar'),
    
    path('luMarketplace_ativar/<id_prod>', views.luMarketplace_ativar, name='luMarketplace-ativar'),

]
