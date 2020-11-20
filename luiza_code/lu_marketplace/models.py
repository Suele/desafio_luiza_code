from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from django.urls import reverse



class Produto(models.Model):
    prod_codigo = models.AutoField(primary_key=True)
    prod_nome = models.CharField(max_length=100, verbose_name='Nome')
    prod_descricao = models.TextField(max_length=100, verbose_name='Descrição')
    prod_preco = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Preço')
    prod_qtd = models.IntegerField(verbose_name='Quantidade')
    prod_inativo = models.BooleanField(default=False, verbose_name='Produto Inativo')
    vend_id = models.ForeignKey(User, on_delete=CASCADE, verbose_name='Vendedor')

    def __str__(self) -> str:
        return self.prod_nome
    