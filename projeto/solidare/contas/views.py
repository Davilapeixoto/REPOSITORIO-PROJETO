from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import func_usuarios

# Create your views here.

def cadastro(request):
    if request.method =="POST":
        id=request.POST.get("id")
        email=request.POST.get("email")
        senha=request.POST.get("senha")
        tipo_usuario=request.POST.get("tipo_usuario")
        nome=request.POST.get("nome")
        sobrenome=request.POST.get("sobrenome")
        if id and email and senha and tipo_usuario and nome and sobrenome:
            user= func_usuarios(id=id,email=email,tipo_usuario=tipo_usuario,nome=nome,sobrenome=sobrenome)
            user.save()
            login(request,user)
            return redirect("login")
        
    return render(request,'contas/cadastro.html')