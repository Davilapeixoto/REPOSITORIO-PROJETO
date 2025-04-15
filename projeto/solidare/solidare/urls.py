"""
URL configuration for solidare project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from contas.views import home,fazer_logout,fazer_login,cadastro,area_admin,area_aluno,area_patrocinador,area_professor
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('login/',fazer_login,name='login'),
    path('logout/', fazer_logout, name='logout'),
    path('cadastro/',cadastro,name='cadastro'),
    path('area_aluno/', area_aluno, name='area_aluno'),
    path('area_professor/', area_professor, name='area_professor'),
    path('area_admin/', area_admin, name='area_admin'),
    path('area_patrocinador/', area_patrocinador, name='area_patrocinador'),
    path('', views.dashboard, name='dashboard'),
    path('area-aluno/', views.area_aluno, name='area_aluno'),

]



