from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Equipamentos

# Início
def home(request):
    return render(request, 'app/globals/home.html')

# Sessão de equipamentos
def cadastrar_equipamentos(request):
    if request.method == 'POST':
        equipamento = request.POST.get('equipamento')
        quantidade = request.POST.get('quantidade')
        print(f'Equipamento: {equipamento}, Quantidade: {quantidade}')
        if equipamento and quantidade:
            Equipamentos.objects.create(equipamento=equipamento, quantidade=quantidade)
    return render(request, 'app/globals/cadastrar_equipamentos.html')


def editar_equipamentos(request):
    values = Equipamentos.objects.all()
    equipamento = request.GET.get('equipamento')
    if equipamento:
        values = values.filter(equipamento__icontains=equipamento)
    return render(request, 'app/globals/editar_equipamentos.html', {'equipamentos': values})

def deletar_equipamento(request, equipamento_id):
    equipamento = get_object_or_404(Equipamentos, id=equipamento_id)
    equipamento.delete()
    messages.success(request, 'Equipamento deletado com sucesso!') 
    return redirect('editar') 



def editar_equipamento(request, equipamento_id):
    equipamento = get_object_or_404(Equipamentos, id=equipamento_id)
    if request.method == 'POST':
        novo_nome = request.POST.get('equipamento')
        nova_quantidade = request.POST.get('quantidade')

        if novo_nome and nova_quantidade:
            try:
                nova_quantidade = int(nova_quantidade)
                equipamento.equipamento = novo_nome
                equipamento.quantidade = nova_quantidade
                equipamento.save()
                messages.success(request, 'Equipamento atualizado com sucesso!')
                return redirect('editar')
            except Exception as e:
                messages.error(request, f'Erro ao salvar: {e}')
        else:
            messages.error(request, 'Todos os campos são obrigatórios.')

    return render(request, 'app/globals/editar_equipamento.html', {'equipamento': equipamento})

# Sessão EPI
def relatorios_epi(request):
    return render(request, 'app/globals/relatorios_epi.html')

def registrar_acao(request):
    return render(request, 'app/globals/registrar_acao.html')



def cadastrar_colaborador(request):
    return render(request, 'app/globals/cadastrar_colaborador.html')

def relatorios_colaborador(request):
    return render(request, 'app/globals/relatorios_colaborador.html')

def editar_colaborador(request):
    return render(request, 'app/globals/editar_colaborador.html')









