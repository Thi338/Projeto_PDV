from django.test import TestCase

from ...models import Cliente

# Create your tests here.


class ClienteTestCase(TestCase):

    def setUp(self):
        Cliente.objects.create(
            nome_do_cliente = "João Nogueira",
            endereco = "Rua Osvaldo W. Fehr",
            telefone = 11993394938

        )

    def test_retorno_str(self):
        c1 = Cliente.objects.get(nome_do_cliente="João Nogueira")
        self.assertEquals(c1.__str__(), "João Nogueira")


