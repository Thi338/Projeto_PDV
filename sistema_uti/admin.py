from django.contrib import admin
from django.http import HttpResponse, response
from django.db.models import Sum
from sistema_uti.models import Produto
from sistema_uti.models import Cliente
from sistema_uti.models import entrada_e_saida
from admin_extra_buttons.api import ExtraButtonsMixin, button, confirm_action, link, view
from admin_extra_buttons.utils import HttpResponseRedirectToReferrer
from reportlab.pdfgen import canvas

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


class OS(ExtraButtonsMixin, admin.ModelAdmin):
    list_display = ('id','data', 'venda_servico', 'n_da_os', 'descricao', 'saida', 'entrada', 'forma_de_pagamento', 'parcelas','codigo_de_barras', 'observacao')
    search_fields = ('id', 'codigo_de_barras')

    @button(permission='demo.add_demomodel1',
            change_form=True,
            html_attrs={'style': 'background-color:#88FF88;color:black'})
    def gerar_relatorio(self, request):
       
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename=relatorio.pdf'

        
        p = canvas.Canvas(response)

        
        p.drawString(190, 800, "TOTAL DE VENDAS POR PRODUTO")
        
        p.drawString(50, 750, "Capinha: ")
        filtroCapinha = entrada_e_saida.objects.filter(descricao__startswith='Capinha').aggregate(Sum('entrada'))
        p.drawString(50, 730, "{}".format(filtroCapinha['entrada__sum']))

        p.drawString(50, 690, "Película: ")
        filtroPelicula = entrada_e_saida.objects.filter(descricao__startswith='Película').aggregate(Sum('entrada'))
        p.drawString(50, 670, "{}".format(filtroPelicula['entrada__sum']))

        p.drawString(50, 630, "Fone de Ouvido: ")
        filtroFone =  entrada_e_saida.objects.filter(descricao__startswith='Fone de Ouvido').aggregate(Sum('entrada'))
        p.drawString(50, 610, "{}".format(filtroFone['entrada__sum']))

        p.drawString(50, 570, "Smartphone: ")
        filtroSmartphone =  entrada_e_saida.objects.filter(descricao__startswith='Smartphone').aggregate(Sum('entrada'))
        p.drawString(50, 550, "{}".format(filtroSmartphone['entrada__sum']))

        p.showPage()
        p.save()
        return response

admin.site.register(entrada_e_saida, OS)





admin.site.site_header = 'UTI CELL'

