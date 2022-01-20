from django.test import TestCase

from ...models import Produto


class ProdutoTestCase(TestCase):

    def setUp(self):
        Produto.objects.create(
            nome_do_produto="Iphone 10",
            codigo_de_barras = 1234567891059,
            quantidade = 1,
            preco = 1500
        )

        def test_retorno_str(self):
            p1 = Produto.objects.get(nome_do_produto="Iphone 10")
            self.assertEquals(p1.__str__(), "Iphone")