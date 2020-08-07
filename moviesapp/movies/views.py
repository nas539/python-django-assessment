# -*- coding: utf-8 -*-

"""Movies views."""

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.shortcuts import redirect
from django.http import Http404
from django.urls import reverse_lazy

from .models import Movie


class MovieListView(ListView):
    """Show all movies."""

    # model = Movie
    template_name = 'movies/movie_list.html'
   

    def get_queryset(self):
        return Movie.objects.order_by('-year')
    


class MovieDetailView(DetailView):
    """Show the requested movie."""

    model = Movie
    template_name = 'movies/movie_detail.html'


class MovieCreateView(CreateView):
    """Create a new movie."""


class MovieUpdateView(UpdateView):
    """Update the requested movie."""


class MovieDeleteView(DeleteView):
    """Delete the requested movie."""
