from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from functools import wraps
from .models import func_usuarios
from django.contrib import messages
from alunos.models import Desempenho

# Create your views here.

def home(request):
    return render(request, 'contas/home.html')

def cadastro(request):
    if request.method == "POST":
        username = request.POST.get("id_usuario")
        email = request.POST.get("email")
        senha = request.POST.get("senha")
        tipo_usuario = request.POST.get("tipo_usuario")
        first_name = request.POST.get("nome")
        last_name = request.POST.get("sobrenome")

        if username and email and senha and tipo_usuario and first_name and last_name:
            usuario = func_usuarios(
                username=username,
                email=email,
                tipo_usuario=tipo_usuario,
                first_name=first_name,
                last_name=last_name 
            )
            usuario.set_password(senha)
            usuario.save()
            login(request, usuario)
            return redirect("login")

    return render(request, "contas/cadastro.html")



def fazer_login(request):
    if request.POST: 
        username = request.POST.get('id_usuario')
        senha = request.POST.get('senha')

        usuario=authenticate(request,username=username,password=senha)

        if usuario is not None:
            login(request, usuario)
            if usuario.tipo_usuario == 'aluno':
                return redirect('area_aluno')
            elif usuario.tipo_usuario == 'professor':
                return redirect('area_professor')
            elif usuario.tipo_usuario == 'admin':
                return redirect('area_admin')
            elif usuario.tipo_usuario == 'patrocinador':
                return redirect('area_patrocinador')
            else:
                return redirect('home')
            
        else:
            messages.error(request, "Usuario ou senha invalido")
            return redirect('login')
        
    return render(request, 'contas/login.html')

def fazer_logout(request):
    logout(request)
    return redirect('login')

def tipo_requerido(tipo):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return redirect('login')
            if getattr(request.user, 'tipo_usuario', None) != tipo:
                return redirect('home')
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator

@tipo_requerido('professor')
def area_professor(request):
    return render(request, 'contas/area_professor.html')

@tipo_requerido('aluno')
def area_aluno(request):
    cursos = request.user.cursos.all()
    desempenhos = Desempenho.objects.filter(aluno=request.user)
    for desempenho in desempenhos:
        if desempenho.nota >= 7:
            desempenho.status = 'Bom'
        elif 5 <= desempenho.nota < 7:
            desempenho.status = 'Regular'
        else:
            desempenho.status = 'Ruim'
    return render(request, 'contas/area_aluno.html', {'cursos': cursos})

@tipo_requerido('admin')
def area_admin(request):
    return render(request, 'contas/area_admin.html')

@tipo_requerido('patrocinador')
def area_patrocinador(request):
    return render(request, 'contas/area_patrocinador.html')

from django.shortcuts import render
from .models import Produto

def dashboard(request):
    produtos = Produto.objects.all()
    return render(request, 'template.html', {'produtos': produtos})
