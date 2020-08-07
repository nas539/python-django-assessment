# -*- coding: utf-8 -*-
from django.urls import path, include

from . import views

movies_patterns = ([
   path('', view=views.MovieListView.as_view(), name='index'),
    path('(<int:id>/',
         view=views.MovieDetailView.as_view(), name='detail'),
    path('create/', view=views.MovieCreateView.as_view(), name='create'),
    path('update/<int:id>/',
         view=views.MovieUpdateView.as_view(), name='update'),
    path('delete/<int:id>/',
         view=views.MovieDeleteView.as_view(), name='delete')
], 'movies')

urlpatterns = [
    path('movies/', include(movies_patterns)),
]
