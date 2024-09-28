from django.shortcuts import render
from app.models import Equipamentos

# Create your views here.

def home(request):
    return render(request, 'app/globals/home.html')

def form_imprestimo(request):
    return render(request, 'app/globals/controle_epi.html')

def cadastrar_equipamentos(request):
    if request.method == 'POST':
        equipamento = request.POST.get('equipamento')
        quantidade = request.POST.get('quantidade')
        print(f'Equipamento: {equipamento}, Quantidade: {quantidade}')  # Debugging
        if equipamento and quantidade:
            Equipamentos.objects.create(equipamento=equipamento, quantidade=quantidade)
            # Redirecionar ou renderizar uma página de sucesso
    return render(request, 'app/globals/cadastrar_equipamentos.html')

def listar_equipamentos(request):
    values = Equipamentos.objects.all()
    equipamento = request.GET.get('equipamento')
    if equipamento:
        values = values.filter(equipamento__icontains=equipamento)
    return render(request, 'app/globals/cadastrar_equipamentos')


