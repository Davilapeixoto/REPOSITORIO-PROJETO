from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from functools import wraps
from .models import func_usuarios

# Create your views here.

def cadastro(request):
    if request.method =="POST":
        id_usuario=request.POST.get("id_usuario")
        email=request.POST.get("email")
        senha=request.POST.get("senha")
        tipo_usuario=request.POST.get("tipo_usuario")
        nome=request.POST.get("nome")
        sobrenome=request.POST.get("sobrenome")
        if id_usuario and email and senha and tipo_usuario and nome and sobrenome:
            usuario= func_usuarios(id_usuario=id_usuario,email=email,tipo_usuario=tipo_usuario,nome=nome,sobrenome=sobrenome)
            usuario.set_password(senha)
            usuario.save()
            login(request,usuario)
            return redirect("login")
        
    return render(request,'contas/cadastro.html')

def fazer_login(request):
    if request.POST: 
        id_usuario = request.POST.get('id_usuario')
        senha = request.POST.get('senha')
        usuario=authenticate(request,id_usuario=id_usuario,senha=senha)
        if usuario is not None:
            login(request,usuario)
            return redirect('/')
        else:
            messages.error(request, "Usuario ou senha invalido")
            return redirect('contas/login.html')
        
    return render(request, 'contas/login.html')

def fazer_logout(request):
    logout(request)
    return redirect('login')

@login_required
def autenticador(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    if request.user.tipo_usuario=='aluno':
        return redirect('area_aluno')
    elif request.user.tipo_usuario=='professor':
        return redirect('area_professor')
    elif request.user.tipo_usuario=='admin':
        return redirect('area_admin')
    else:
        return redirect('area_patrocinador')
    
