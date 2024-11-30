import pytest
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from app.models import Equipamentos, Cadastro_Colaboradores, Acoes


class HomeTest(TestCase):
# Testes Unitários
    def test_home(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

class CadastrarColaboradorTest(TestCase):
    def test_cadastrar_colaborador(self):
        response = self.client.get(reverse('cadastrar_colaborador'))
        self.assertEqual(response.status_code, 200)

class CadastrarEquipamentosTest(TestCase):
    def test_cadastrar_equipamentos(self):
        response = self.client.get(reverse('cadastrar_equipamentos'))
        self.assertEqual(response.status_code, 200)

class RegistrarAcaoTest(TestCase):
    def test_registrar_acao(self):
        response = self.client.get(reverse('registrar_acao'))
        self.assertEqual(response.status_code, 200)

class EditarColaboradoresTest(TestCase):
    def test_editar_colaboradores(self):
        response = self.client.get(reverse('editar_colaboradores'))
        self.assertEqual(response.status_code, 200)

class EditarEquipamentosTest(TestCase):
    def test_editar_equipamentos(self):
        response = self.client.get(reverse('editar_equipamentos'))
        self.assertEqual(response.status_code, 200)

class RelatoriosColaboradorTest(TestCase):
    def test_relatorios_colaborador(self):
        response = self.client.get(reverse('relatorios_colaborador'))
        self.assertEqual(response.status_code, 200)

class RelatoriosEpiTest(TestCase):
    def test_relatorios_epi(self):
        response = self.client.get(reverse('relatorio_epi'))
        self.assertEqual(response.status_code, 200)

# Testes Integração
@pytest.mark.django_db
def teste_verificar_informacoes_db_equipamentos(client):
    
    url = reverse('editar_equipamentos')
    response = client.get(url)

    assert response.status_code == 200


@pytest.mark.django_db
def test_enviar_informacoes_equipamento(client):
    data = {
        'equipamento': 'Equipamento 1',
        'quantidade': 10,
    }
    url = reverse('cadastrar_equipamentos')

    response = client.post(url, data)

    assert response.status_code == 302

    assert response.url == reverse('editar_equipamentos')

    equipamento = Equipamentos.objects.get(equipamento='Equipamento 1')
    assert equipamento.quantidade == 10

    response = client.get(reverse('editar_equipamentos'))
    assert 'Equipamento 1' in response.content.decode()
    assert 'Quantidade: 10' in response.content.decode()

@pytest.mark.django_db
def teste_verificar_informacoes_db_colaboradores(client):
    
    url = reverse('editar_colaboradores')
    response = client.get(url)

    assert response.status_code == 200

@pytest.mark.django_db
def test_enviar_informacoes_colaborador(client):
    data = {
        'colaborador': 'colaborador 1',
        'matricula': '123',
        'senha': '123',
    }
    url = reverse('cadastrar_colaborador')

    response = client.post(url, data)

    assert response.status_code == 302

    assert response.url == reverse('editar_colaboradores')

    colaborador = Cadastro_Colaboradores.objects.get(colaborador='colaborador 1')
    assert colaborador.matricula == '123'
    assert colaborador.senha == '123'

    response = client.get(reverse('editar_colaboradores'))
    assert 'colaborador 1' in response.content.decode()
    assert '123' in response.content.decode()
    assert '123' in response.content.decode()


