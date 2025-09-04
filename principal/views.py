from django.shortcuts import render, get_object_or_404
from .models import Disciplina, Entrenador, Post

def home(request):
    disciplinas = Disciplina.objects.all()
    posts = Post.objects.order_by('-fecha_publicacion')[:2] # Obtenemos los 2 posts más recientes
    return render(request, 'principal/home.html', {'disciplinas': disciplinas, 'posts': posts})

def disciplinas(request):
    disciplinas = Disciplina.objects.all()
    return render(request, 'principal/disciplinas.html', {'disciplinas': disciplinas})

def entrenadores(request):
    entrenadores = Entrenador.objects.all()
    return render(request, 'principal/entrenadores.html', {'entrenadores': entrenadores})

def disciplina_detalle(request, disciplina_id):
    disciplina = get_object_or_404(Disciplina, pk=disciplina_id)
    return render(request, 'principal/disciplina_detalle.html', {'disciplina': disciplina})

def blog(request):
    posts = Post.objects.all().order_by('-fecha_publicacion')
    return render(request, 'principal/blog.html', {'posts': posts})

def post_detalle(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'principal/post_detalle.html', {'post': post})