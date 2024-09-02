from django.shortcuts import render
from Aluno.forms import *
from Aluno.models import *
# Create your views here.
def cadastro_aluno(request):
    alunos = Aluno.objects.all()
    if request.method == "POST":
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            form = AlunoForm()
    else:
        form = AlunoForm()
    return render(request, 'form.html', {'alunos':alunos, 'form': form})