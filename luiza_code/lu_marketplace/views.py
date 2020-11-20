from django.shortcuts import render
from django.http import HttpResponse
from . models import Produto
from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin



def index(request):
    produtos = Produto.objects.all()
    listaProdutos = Produto.objects.all()
    search = request.GET.get('search')
    if search:
        produtos = produtos.filter(prod_nome__icontains=search)

    context = {'produtos': produtos, 'listaProdutos': listaProdutos}
    return render(request, 'lu_marketplace/index.html', context)



class CadastrarProduto(SuccessMessageMixin, CreateView):
    model = Produto
    template_name = 'cadastrar_prod.html'
    fields = '__all__'
    success_message = 'Produto cadastrado com sucesso!'
    def get_success_url(self):  
        return '/'

class AtualizarProduto(SuccessMessageMixin, CreateView):
    model = Produto
    template_name = 'atualizar_prod.html'
    fields = '__all__'
    success_message = 'Produto atualizado com sucesso!'
    def get_success_url(self):  
        return '/'

def luMarketplace_deletar(request, id_prod):
    Produto.objects.filter(prod_codigo=id_prod).delete()
    produtos = Produto.objects.all()
    listaProdutos = Produto.objects.all()
    context = {'produtos': produtos, 'listaProdutos': listaProdutos}
    return render(request, 'lu_marketplace/index.html', context)

def luMarketplace_inativar(request, id_prod):
    Produto.objects.filter(prod_codigo=id_prod).update(prod_inativo=True)
    produtos = Produto.objects.all()
    listaProdutos = Produto.objects.all()
    context = {'produtos': produtos, 'listaProdutos': listaProdutos}
    return render(request, 'lu_marketplace/index.html', context)

def luMarketplace_ativar(request, id_prod):
    Produto.objects.filter(prod_codigo=id_prod).update(prod_inativo=False)
    produtos = Produto.objects.all()
    listaProdutos = Produto.objects.all()
    context = {'produtos': produtos, 'listaProdutos': listaProdutos}
    return render(request, 'lu_marketplace/index.html', context)