from django.db import models
from datetime import datetime, date

class Produto(models.Model):
    nome_do_produto = models.CharField(max_length=30)
    codigo_de_barras = models.CharField(max_length=13)
    quantidade = models.CharField(max_length=3)
    preco = models.CharField(max_length=7)
    

    def __str__(self):
        return self.nome_do_produto

class Cliente(models.Model):
    nome_do_cliente = models.CharField(max_length=30)
    endereco = models.CharField(max_length=60)
    telefone = models.CharField(max_length=11)

    def __str__(self):
        return self.nome_do_cliente

class entrada_e_saida(models.Model):
    VENDA_CHOICES = (
        ("V", "VENDA"),
        ("S", "SERVIÇO")
    )
    PAGAMENTO_CHOICES = (
        ("D", "DÉBITO"),
        ("C", "CRÉDITO"),
        ("DN", "DINHEIRO"),
        ("P", "PIX"),
    )
    
    PARCELAS_CHOICES = (
        ("AV", "Á VISTA"),
        ("2", "2x"),
        ("3", "3x")
    )
    data = models.DateField(default=datetime.now)
    venda_servico = models.CharField(max_length=1, choices=VENDA_CHOICES, blank=False, null=False)
    codigo_de_barras = models.CharField(max_length=13)
    n_da_os = models.CharField(max_length=4)
    descricao = models.TextField()
    saida = models.CharField(max_length=6)
    entrada = models.CharField(max_length=6)
    forma_de_pagamento = models.CharField(max_length=15, choices=PAGAMENTO_CHOICES, blank=False, null=False)
    parcelas = models.CharField(max_length=2, choices=PARCELAS_CHOICES, blank=False, null=False)
    observacao = models.TextField()

    
   
    

    def __str__(self):
        return self.codigo_de_barras
   