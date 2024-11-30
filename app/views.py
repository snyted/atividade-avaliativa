from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import JsonResponse
from .models import Equipamentos, Cadastro_Colaboradores, Acoes

# Início
def home(request):
    return render(request, 'app/globals/home.html')

# Sessão de equipamentos
def cadastrar_equipamentos(request):
    if request.method == 'POST':
        equipamento = request.POST.get('equipamento')
        quantidade = request.POST.get('quantidade')
        if equipamento and quantidade:
            Equipamentos.objects.create(equipamento=equipamento, quantidade=quantidade)
            return redirect('editar_equipamentos')
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
    return redirect('editar_equipamentos') 



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
                return redirect('editar_equipamentos')
            except Exception as e:
                messages.error(request, f'Erro ao salvar: {e}')
        else:
            messages.error(request, 'Todos os campos são obrigatórios.')

    return render(request, 'app/globals/editar_equipamento.html', {'equipamento': equipamento})

def verificar_equipamento(request):
    equipamento = request.GET.get('equipamento')
    exists = Equipamentos.objects.filter(equipamento=equipamento).exists()
    return JsonResponse({'exists': exists})

# Sessão EPI
def verificar_colaborador(request):
    colaborador = request.GET.get('colaborador')
    exists = Cadastro_Colaboradores.objects.filter(colaborador=colaborador).exists()
    return JsonResponse({'exists': exists})

def registrar_acao(request):
    if request.method == 'POST':
        colaborador = request.POST.get('colaborador')
        equipamento = request.POST.get('equipamento')
        dataEmprestimo = request.POST.get('dataEmprestimo')
        dataDevolucao = request.POST.get('dataDevolucao')
        status = request.POST.get('status')
        condicoes = request.POST.get('condicoes')
        dataDevolucaoReal = request.POST.get('dataDevolucaoReal', None)
        observacoes = request.POST.get('observacoes', '')

        if Cadastro_Colaboradores.objects.filter(colaborador=colaborador).exists() and Equipamentos.objects.filter(equipamento=equipamento).exists():
            acao = Acoes(
                colaborador=Cadastro_Colaboradores.objects.get(colaborador=colaborador),
                equipamento=Equipamentos.objects.get(equipamento=equipamento),
                dataEmprestimo=dataEmprestimo,
                dataDevolucao=dataDevolucao,
                status=status,
                condicoes=condicoes,
                dataDevolucaoReal=dataDevolucaoReal,
                observacoes=observacoes
            )
            acao.save()
            return redirect('registrar_acao')
        else:
            return render(request, 'app/globals/registrar_acao.html', {'error': 'Colaborador ou Equipamento não encontrado'})
    return render(request, 'app/globals/registrar_acao.html')

def relatorios_epi(request):
    acoes = Acoes.objects.all()
    return render(request, 'app/globals/relatorios_epi.html', {'acoes': acoes})


# Sessão Colaborador
def cadastrar_colaborador(request):
    if request.method == 'POST':
        colaborador = request.POST.get('colaborador')
        matricula = request.POST.get('matricula')
        senha = request.POST.get('senha')
        print(f'Colaborador: {colaborador}, Matricula: {matricula}, Senha: {senha}')
        Cadastro_Colaboradores.objects.create(colaborador=colaborador, matricula=matricula, senha=senha)
        return redirect('editar_colaboradores')
    return render(request, 'app/globals/cadastrar_colaborador.html')

def relatorios_colaborador(request):
    return render(request, 'app/globals/relatorios_colaborador.html')



def editar_colaboradores(request):
    values = Cadastro_Colaboradores.objects.all()
    colaborador_filtro = request.GET.get('colaborador')
    if colaborador_filtro:
        values = values.filter(colaborador__icontains=colaborador_filtro)
    return render(request, 'app/globals/editar_colaboradores.html', {'colaboradores': values})

def editar_colaborador(request, colaborador_id):
    colaborador = get_object_or_404(Cadastro_Colaboradores, id=colaborador_id)
    if request.method == 'POST':
        novo_colaborador = request.POST.get('colaborador')
        nova_matricula = request.POST.get('matricula')
        nova_senha = request.POST.get('senha')
        
        if novo_colaborador and nova_matricula and nova_senha:
            try:
                colaborador.colaborador = novo_colaborador
                colaborador.matricula = nova_matricula
                colaborador.senha = nova_senha
                colaborador.save()
                messages.success(request, 'Colaborador atualizado com sucesso!')
                return redirect('editar_colaboradores')
            except Exception as e:
                messages.error(request, f'Erro ao salvar: {e}')
        else:
            messages.error(request, 'Todos os campos são obrigatórios.')

    return render(request, 'app/globals/editar_colaborador.html', {'colaborador': colaborador})

def deletar_colaborador(request, colaborador_id):
    colaborador = get_object_or_404(Cadastro_Colaboradores, id=colaborador_id)
    colaborador.delete()
    messages.success(request, 'Colaborador deletado com sucesso!')
    return redirect('editar_colaboradores')

def relatorios_colaborador(request):
    acoes = Acoes.objects.all()
    return render(request, 'app/globals/relatorios_colaborador.html', {'acoes': acoes})








