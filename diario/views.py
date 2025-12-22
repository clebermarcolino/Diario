from django.shortcuts import get_object_or_404, render, redirect
from .models import Pessoa, Diario
from datetime import datetime, timedelta, date
from django.contrib import messages  


def home(request):
    textos = Diario.objects.all().order_by('-create_at')[:3] #  Busca no banco de dados os 3 diários mais recentes, ordenados por data de criação.
    pessoas = Pessoa.objects.all() # Busca todas as pessoas registradas no banco.
    nomes = [pessoa.nome for pessoa in pessoas] # Cria uma lista com os nomes de todas as pessoas.
    quantidades = []
    for pessoa in pessoas:
        quantidade = Diario.objects.filter(pessoas=pessoa).count() # calcula quantos diários estão associados a cada pessoa
        quantidades.append(quantidade)
    
    return render(request, 'home.html', {'textos': textos, 'nomes': nomes, 'quantidades': quantidades}) # Renderiza o template home.html, passando as listas textos, nomes, e quantidades como variáveis para serem usadas no template.

def escrever(request):
    if request.method == 'GET':
        pessoas = Pessoa.objects.all()
        return render(request, 'escrever.html', {'pessoas': pessoas})
    elif request.method == 'POST':
        titulo = request.POST.get('titulo')
        tags = request.POST.getlist('tags')
        pessoas = request.POST.getlist('pessoas')
        texto = request.POST.get('texto')
        
            
        if len(titulo.strip()) == 0 or len(texto.strip()) == 0:
            messages.error(request, '⚠️ Título e texto não podem ser vazios!')
            return redirect('escrever')

        if not pessoas:  
            messages.error(request, '⚠️ Você deve selecionar uma pessoa!')
            return redirect('escrever')
        
        if not tags:  
            messages.error(request, '⚠️ Uma tag deve ser selecionada!')
            return redirect('escrever')
        
        diario = Diario(
            titulo=titulo,
            texto=texto
        )
        
        diario.set_tags(tags)
        diario.save()

        for i in pessoas:
            pessoa = Pessoa.objects.get(id=i)
            diario.pessoas.add(pessoa)

        diario.save()
 
        messages.success(request, '✅ Sua anotação foi salva com sucesso!')
        return redirect('escrever')
    
def cadastrar_pessoa(request):
    if request.method == 'GET':
        pessoas = Pessoa.objects.all()
        return render(request, 'pessoa.html', {'pessoas': pessoas})
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        foto = request.FILES.get('foto')

        if len(nome.strip()) == 0:
            messages.error(request, '⚠️ O nome da pessoa não pode estar vazio.')
            return redirect('cadastrar_pessoa')
        
        if foto:
            extensoes_validas = ['jpg', 'jpeg', 'png']
            ext = foto.name.split('.')[-1].lower()
            if ext not in extensoes_validas:
                messages.error(request, '⚠️ O arquivo enviado não é uma imagem válida (use JPG, JPEG, PNG).')
                return redirect('cadastrar_pessoa')

        pessoa = Pessoa(
            nome=nome,
            foto=foto
        )

        pessoa.save()
        messages.success(request, '✅ Pessoa cadastrada com sucesso!')
        return redirect('cadastrar_pessoa')
    
def excluir_pessoa(request, pessoa_id):
        pessoa = Pessoa.objects.get(id=pessoa_id)
        pessoa.delete()
        messages.success(request, '✅ Pessoa excluída com sucesso!')
        return redirect('listar_pessoas')

def listar_pessoas(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'pessoa.html', {'pessoas': pessoas})

def dia(request):
    data_str = request.GET.get('data')
    
    if data_str:
        try:
            data_formatada = datetime.strptime(data_str, '%Y-%m-%d')
        except ValueError:
            data_formatada = datetime.combine(date.today(), datetime.min.time())
    else:
        data_formatada = datetime.combine(date.today(), datetime.min.time())
    
    inicio_do_dia = data_formatada
    fim_do_dia = data_formatada + timedelta(days=1)
    
    diarios = Diario.objects.filter(create_at__gte=inicio_do_dia, create_at__lt=fim_do_dia).order_by('create_at')
    
    data_para_template = data_formatada.strftime('%Y-%m-%d')
    
    return render(request, 'dia.html', {
        'diarios': diarios,
        'total': diarios.count(),
        'data': data_para_template,
    })

def excluir_anotacao_dia(request): # metódo para excluir todas as anotações de um dia selecionado
    dia = datetime.strptime(request.GET.get('data'), '%Y-%m-%d')
    diarios = Diario.objects.filter(create_at__gte=dia).filter(create_at__lte=dia + timedelta(days=1))
    diarios.delete()
    messages.success(request, "✅ Todas as anotações foram excluídas com sucesso!")
    return redirect('escrever')

def excluir_anotacao_individual(request, id): # metódo para excluir uma anotação de um dia selecionado
    anotacao = get_object_or_404(Diario, id=id)
    next_url = request.GET.get('next') or reverse('escrever')

    if not next_url.startswith('/') or next_url.startswith('//'):
        next_url = reverse('escrever')

    anotacao.delete()
    messages.success(request, "✅ Anotação excluída com sucesso!")
    return redirect(next_url)