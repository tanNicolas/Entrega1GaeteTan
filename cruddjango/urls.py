"""cruddjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from juegos import views as views_juegos
from peliculas import views as views_peliculas
from libros import views as views_libros
from buscador import views as views_buscador

urlpatterns = [
    path('admin/', admin.site.urls),

    # Juegos
    path('juegos', views_juegos.juegos_index),
    path('juegos/add', views_juegos.juegos_add),
    path('juegos/edit/<int:id>', views_juegos.juegos_edit),
    path('juegos/update/<int:id>', views_juegos.juegos_update),
    path('juegos/delete/<int:id>', views_juegos.juegos_destroy),

    # Peliculas
    path('peliculas', views_peliculas.peliculas_index),
    path('peliculas/add', views_peliculas.peliculas_add),
    path('peliculas/edit/<int:id>', views_peliculas.peliculas_edit),
    path('peliculas/update/<int:id>', views_peliculas.peliculas_update),
    path('peliculas/delete/<int:id>', views_peliculas.peliculas_destroy),

    # Libros
    path('libros', views_libros.libros_index),
    path('libros/add', views_libros.libros_add),
    path('libros/edit/<int:id>', views_libros.libros_edit),
    path('libros/update/<int:id>', views_libros.libros_update),
    path('libros/delete/<int:id>', views_libros.libros_destroy),

    # Buscador
    path('', views_buscador.buscador_index),
    path('resultados', views_buscador.buscador_resultado),
]
