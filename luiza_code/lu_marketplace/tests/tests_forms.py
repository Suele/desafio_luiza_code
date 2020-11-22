from django.test import TestCase
from ..forms import CadastraProduto
from django.contrib.auth.models import User

# Create your tests here.
class CadastrarFormTestCase(TestCase):
    def test_cadastrar_form_val(self):
        form = CadastraProduto(data={
           'prod_nome': 'Feijao', 
           'prod_descricao': 'Grau preto e marrom',
           'prod_preco': 6, 
           'prod_codigo': 2, 
           'prod_qtd': 100, 
           'prod_inativo': False, 
           'vend_id': 'gerente'
        })
        self.assertTrue(form.is_valid())