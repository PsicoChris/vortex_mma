from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('disciplinas/', views.disciplinas, name='disciplinas'),
    path('entrenadores/', views.entrenadores, name='entrenadores'),
    path('disciplinas/<int:disciplina_id>/', views.disciplina_detalle, name='disciplina_detalle'),
    path('blog/', views.blog, name='blog'),
    path('blog/<int:post_id>/', views.post_detalle, name='post_detalle'),

]