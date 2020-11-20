from django.shortcuts import render
from django.http import HttpResponse
from . models import Produto
from django.views.generic import CreateView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from . forms import CadastraProduto
from django.shortcuts import get_object_or_404,redirect




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

def luMarketplace_atualizar(request, id):
    p = get_object_or_404(Produto, pk=id)
    form = CadastraProduto(instance=p)
    if(request.method == 'POST'):
        form = CadastraProduto(request.POST, instance=p)
        
        if(form.is_valid()): #valida o formulário
            p = form.save(commit=False)
            p.prod_nome = form.cleaned_data['prod_nome']
            p.prod_descricao = form.cleaned_data['prod_descricao']
            p.prod_preco = form.cleaned_data['prod_preco']
            p.prod_qtd = form.cleaned_data['prod_qtd']
            p.prod_inativo = form.cleaned_data['prod_inativo']
            p.vend_id = form.cleaned_data['vend_id']
            p.save()
            return redirect('/')
        else:
            return render(request, 'atualizar_prod.html', {'form': form, 'p' : p})
    elif(request.method == 'GET'):
        return render(request, 'atualizar_prod.html', {'form': form, 'p' : p})
  
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