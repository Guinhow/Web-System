from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import FormularioDados
from .forms import ConsultaForm
from .models import DadosFormulario
from django.shortcuts import get_object_or_404, redirect

def home(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_page = request.POST.get('next', None)
            if next_page:
                return redirect(next_page)
            else:
                return redirect('Página Inicial')
        else:
            messages.error(request, 'Credenciais inválidas. Tente novamente.')
            return render(request, 'registration/login.html')
    else:
        return render(request, 'registration/login.html')

@login_required
def restrita(request):
    return render(request, 'main/inicio.html')

# @login_required
# def filtroAmostra(request):
#     return render(request, 'main/filtroAmostra.html')

@login_required
def resultados(request):
    return render(request, 'main/resultados.html')

@login_required
def filtroAresultados(request):
    return render(request, 'main/filtroAresultados.html')

@login_required
def laudos(request):
    return render(request, 'main/laudos.html')

@login_required
def saidaAmostra(request):
    return render(request, 'main/saidaAmostra.html')

@login_required
def filtrosaida(request):
    return render(request, 'main/filtrosaida.html')

@login_required
def cadastro(request):
    return render(request, 'main/cadastro.html')

@login_required
def filtrocadastro(request):
    return render(request, 'main/filtrocadastro.html')

@login_required
def estoque(request):
    return render(request, 'main/estoque.html')

@login_required
def formulario(request):
    if request.method == 'POST':
        form = FormularioDados(request.POST)
        if form.is_valid():
            form.save()
            sucesso_msg = "Os dados foram enviados com sucesso!"
            return render(request, 'main/entradaAmostra.html', {'form': FormularioDados(), 'sucesso_msg': sucesso_msg})
        else:
            return render(request, 'main/entradaAmostra.html', {'form': form, 'erro_msg': "Por favor, preencha todos os campos."})
    else:
        form = FormularioDados()
    return render(request, 'main/entradaAmostra.html', {'form': form})

@login_required
def consultar_dados(request):
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            # id = form.cleaned_data.get('id')
            codigo_bq = form.cleaned_data.get('codigo_bq')
            # data_coleta = form.cleaned_data.get('data_coleta')
            data_entrada = form.cleaned_data.get('data_entrada')
            cliente = form.cleaned_data.get('cliente')
            # codigo_amostra = form.cleaned_data.get('codigo_amostra')
            amostra = form.cleaned_data.get('amostra') 
            # peso = form.cleaned_data.get('peso')
            # temperatura = form.cleaned_data.get('temperatura')
            # classificacao = form.cleaned_data.get('classificacao')
            # obs = form.cleaned_data.get('obs')
            dados = DadosFormulario.objects.all()
            if codigo_bq:
                dados = dados.filter(codigo_bq=codigo_bq)
            if cliente:
                dados = dados.filter(cliente=cliente)
            if amostra:
                dados = dados.filter(amostra=amostra)
            if data_entrada:
                dados = dados.filter(data_entrada=data_entrada)
            sucesso_msg = "Os dados foram enviados com sucesso!"
            return render(request, 'main/filtroAmostra.html', {'dados': dados, 'sucesso_msg': sucesso_msg})
    
            # dados = DadosFormulario.objects.filter(id=id, codigo_bq=codigo_bq, data_coleta=data_coleta, data_entrada=data_entrada, cliente=cliente, codigo_amostra=codigo_amostra, amostra=amostra, peso=peso, temperatura=temperatura, classificacao=classificacao, obs=obs)
            # sucesso_msg = "Os dados foram enviados com sucesso!"
            # return render(request, 'main/filtroAmostra.html', {'dados': dados,'sucesso_msg': sucesso_msg})
    else:
        form = ConsultaForm()
    return render(request, 'main/filtroAmostra.html', {'form': form})


@login_required
def remover_dado(request, dado_id):
    dado = get_object_or_404(DadosFormulario, pk=dado_id)
    if request.method == 'POST':
        dado.delete()
        form = ConsultaForm()
        sucesso_delete = "A entrada foi removida com sucesso."
        return render(request, 'main/inicio.html', {'form': form, 'sucesso_delete': sucesso_delete})
    else:
        form = ConsultaForm()
    return render(request, 'main/inicio.html')