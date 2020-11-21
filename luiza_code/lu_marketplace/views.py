from django.shortcuts import render
from django.http import HttpResponse
from . models import Produto
from django.views.generic import CreateView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . forms import CadastraProduto
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required



def index(request):
    produtos = Produto.objects.all()
    listaProdutos = Produto.objects.all()
    search = request.GET.get('search')
    if (not request.user.is_anonymous):
        vendedor= request.user
        produtos=produtos.filter(vend_id=vendedor)  
        context = {'produtos': produtos, 'listaProdutos': listaProdutos}
        return render(request, 'area_do_vendedor.html', context)

    if search:
        produtos = Produto.objects.filter(prod_nome__icontains=search) 

    context = {'produtos': produtos, 'listaProdutos': listaProdutos}
    return render(request, 'lu_marketplace/index.html', context)

@login_required(login_url='/login/')
def index_logado(request):
    produtos = Produto.objects.all()
    listaProdutos = Produto.objects.all()
    search = request.GET.get('search')
    vendedor= request.user
    if search:
        produtos = Produto.objects.filter(prod_nome__icontains=search)
    produtos=produtos.filter(vend_id=vendedor)   

    context = {'produtos': produtos, 'listaProdutos': listaProdutos}
    return render(request, 'area_do_vendedor.html', context)

class CadastrarProduto(SuccessMessageMixin, CreateView):
    model = Produto
    template_name = 'cadastrar_prod.html'
    fields = '__all__'
    success_message = 'Produto cadastrado com sucesso!'
    def get_success_url(self):
        return '../area_do_vendedor/'



def luMarketplace_atualizar(request, id):
    p = get_object_or_404(Produto, pk=id)
    form = CadastraProduto(instance=p)
    if(request.method == 'POST'):
        form = CadastraProduto(request.POST, instance=p)

        if(form.is_valid()):  # valida o formulário
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
            return render(request, 'atualizar_prod.html', {'form': form, 'p': p})
    elif(request.method == 'GET'):
        return render(request, 'atualizar_prod.html', {'form': form, 'p': p})


def luMarketplace_deletar(request, id_prod):
    Produto.objects.filter(prod_codigo=id_prod).delete()
    produtos = Produto.objects.all()
    listaProdutos = Produto.objects.all()
    vendedor= request.user
    produtos=produtos.filter(vend_id=vendedor)  
    context = {'produtos': produtos, 'listaProdutos': listaProdutos}
    return render(request, 'area_do_vendedor.html', context)

def luMarketplace_inativar(request, id_prod):
    Produto.objects.filter(prod_codigo=id_prod).update(prod_inativo=True)
    produtos = Produto.objects.all()
    listaProdutos = Produto.objects.all()
    vendedor= request.user
    produtos=produtos.filter(vend_id=vendedor)  
    context = {'produtos': produtos, 'listaProdutos': listaProdutos}
    return render(request, 'area_do_vendedor.html', context)


def luMarketplace_ativar(request, id_prod):
    Produto.objects.filter(prod_codigo=id_prod).update(prod_inativo=False)
    produtos = Produto.objects.all()
    listaProdutos = Produto.objects.all()
    vendedor= request.user
    produtos=produtos.filter(vend_id=vendedor)  
    context = {'produtos': produtos, 'listaProdutos': listaProdutos}
    return render(request, 'area_do_vendedor.html', context)


def login_user(request):
    return render(request, 'login.html')


@csrf_protect
def submit_login(request):
    if request.POST:
        user = request.POST.get('user')
        senha = request.POST.get('senha')
        user = authenticate(username=user, password=senha)
        if user is not None:
            login(request, user)
            return redirect('../area_do_vendedor/')
        else:
            messages.error(
                request, "Usuário/Senha incorretas, favor tentar novamente")
    return redirect('/login/')


def logout_user(request):
    logout(request)
    print(request.user)
    return redirect('/')
