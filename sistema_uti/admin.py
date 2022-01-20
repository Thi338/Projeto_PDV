from django.contrib import admin
from sistema_uti.models import Produto
from sistema_uti.models import Cliente
from sistema_uti.models import entrada_e_saida
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import os



class Produtos(admin.ModelAdmin):
    list_display = ('id', 'nome_do_produto','codigo_de_barras', 'quantidade', 'preco')
    list_display_links = ('id', 'nome_do_produto')
    search_fields = ('nome_do_produto', )

admin.site.register(Produto, Produtos)

class Clientes(admin.ModelAdmin):
    list_display = ('id', 'nome_do_cliente', 'endereco', 'telefone')
    list_display_links = ('id', 'nome_do_cliente')
    search_fields = ('nome_do_cliente',)

admin.site.register(Cliente, Clientes)

class OS(admin.ModelAdmin):
    list_display = ('id','data', 'venda_servico', 'n_da_os', 'descricao', 'saida', 'entrada', 'forma_de_pagamento', 'parcelas','codigo_de_barras', 'observacao')
    search_fields = ('id', 'codigo_de_barras')

    actions = ['gerar_os']

    def gerar_os(self):
        pastaApp = os.path.dirname(__file__)
        cnv=canvas.Canvas(pastaApp+"\\ordemservico.pdf", pagesize=A4)
        cnv.save()


admin.site.register(entrada_e_saida, OS)
admin.site.site_header = 'UTI CELL'

