# -*- coding: utf-8 -*-

"""Movies views."""

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.http import Http404
from django.urls import reverse_lazy

from .models import Movie


class MovieListView(ListView):
    """Show all movies."""

    model = Movie
    template_name = 'movies/movie_list.html'
   
    def get_queryset(self, *args, **kwargs): 
        qs = super(MovieListView, self).get_queryset(*args, **kwargs) 
        qs = qs.order_by("-year") 
        return qs 
        
    # def get_queryset(self):
    #     return Movie.objects.order_by('-year')
    


class MovieDetailView(DetailView):
    """Show the requested movie."""

    model = Movie
    template_name = 'movies/movie_detail.html'

    def get_movie_details(self, *args, **kwargs):
        context = super(MovieDetailView, self).get_movie_details(*args, **kwargs)
        rating = context.total_rating / context.number_of_reviews
        return context


class MovieCreateView(SuccessMessageMixin, CreateView):
    """Create a new movie."""
    model = Movie
    template_name = 'movies/movie_form.html'
    # messages.add_message(messages.SUCCESS, 'The movie has been successfully created!')
    # messages.add_message(messages.ERROR, 'The creation has failed.')
    # success_message = 'The movie has been successfully created!'
    # messages.error(request, 'The creation has failed.')
    def create(self, request):
        fields = ["title", "year", "rated", "released_on", "genre", "director", "plot"]
        if self.request:
            return messages.success(self.request, 'The movie has been successfully created!')
        else:
            return messages.error(self.request, 'The creation has failed.')
    
class MovieUpdateView(SuccessMessageMixin, UpdateView):
    """Update the requested movie."""
    model = Movie
    template_name = 'movies/movie_form.html'
    # messages.add_message(messages.SUCCESS, 'The movie has been successfully updated!')
    # messages.add_message(messages.ERROR, 'The update has failed.')
    # success_message = 'The movie has been successfully updated!'
    # messages.error(request, 'The update has failed.')
    def update(self, request):
        fields = ["title", "year", "rated", "released_on", "genre", "director", "plot"]
        if self.request:
            return messages.success(self.request, 'The movie has been successfully updated!')
        else:
            return messages.error(self.request, 'The update has failed.')


class MovieDeleteView(SuccessMessageMixin, DeleteView):
    """Delete the requested movie."""
    model = Movie
    template_name = 'movies/movie_confirm_delete.html'
    # success_message = 'The movie has been successfully deleted!'
    # messages.error(request, 'The deletion has failed.')
    def delete(self, request):
        if self.request:
            return messages.success(self.request, 'The movie has been successfully deleted!')
        else:
            return messages.error(self.request, 'The deletion has failed.')
