from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from app.models import Equipamentos, Cadastro_Colaboradores

def home(request):
    return render(request, 'app/globals/home.html')

def form_imprestimo(request):
    return render(request, 'app/globals/controle_epi.html')

def cadastrar_colaborador(request):
    return render(request, 'app/globals/cadastrar_colaborador.html')

def relatorios_colaborador(request):
    return render(request, 'app/globals/relatorios_colaborador.html')

def editar_colaborador(request):
    return render(request, 'app/globals/editar_colaborador.html')

def cadastro_colaborador(request):
    if request.method == 'POST':
        colaborador = request.POST.get('colaborador')
        matricula = request.POST.get('matricula')
        senha = request.POST.get ('senha')
        print(f'Colaborador: {colaborador}, Matrícula: {matricula}, Senha: {senha}')
        if colaborador and matricula and senha:
            Cadastro_Colaboradores.objects.create(colaborador=colaborador, matricula=matricula, senha=senha)
            return render(request, 'app/globals/cadastrar_colaborador')

def cadastrar_equipamentos(request):
    if request.method == 'POST':
        equipamento = request.POST.get('equipamento')
        quantidade = request.POST.get('quantidade')
        print(f'Equipamento: {equipamento}, Quantidade: {quantidade}')
        if equipamento and quantidade:
            Equipamentos.objects.create(equipamento=equipamento, quantidade=quantidade)
    return render(request, 'app/globals/cadastrar_equipamentos.html')

def listar_equipamentos(request):
    values = Equipamentos.objects.all()
    equipamento = request.GET.get('equipamento')
    if equipamento:
        values = values.filter(equipamento__icontains=equipamento)
    return render(request, 'app/globals/listar_equipamentos.html', {'equipamentos': values})


def deletar_equipamento(request, equipamento_id):
    equipamento = get_object_or_404(Equipamentos, id=equipamento_id)
    equipamento.delete()
    messages.success(request, 'Equipamento deletado com sucesso!') 
    return redirect('editar') 

def editar_equipamento(request):
    if request.method == 'POST':
        equipamento_id = request.POST.get('equipamento_id')
        print(f'Equipamento ID recebido: {equipamento_id}')  # Debugging

        novo_nome = request.POST.get('equipamento')
        nova_quantidade = request.POST.get('quantidade')
        print(f'Novo Nome: {novo_nome}, Nova Quantidade: {nova_quantidade}')  # Debugging

        if equipamento_id:
            # Tente pegar o objeto e atualizá-lo
            try:
                equipamento = get_object_or_404(Equipamentos, id=equipamento_id)
                equipamento.equipamento = novo_nome
                equipamento.quantidade = nova_quantidade
                equipamento.save()

                messages.success(request, 'Equipamento atualizado com sucesso!')
            except Exception as e:
                print(f'Ocorreu um erro: {e}')  # Debugging
        else:
            messages.error(request, 'ID do equipamento não foi fornecido.')

        return redirect('editar')
