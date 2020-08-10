# -*- coding: utf-8 -*-
from django.urls import reverse
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Movie(models.Model):
    title = models.CharField(_('Movie\'s title'), max_length=255)
    year = models.PositiveIntegerField(default=2019)
    # Example: PG-13
    rated = models.CharField(max_length=64)
    released_on = models.DateField(_('Release Date'))
    genre = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    plot = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    total_rating = models.PositiveIntegerField(default=0)
    number_of_reviews = models.PositiveIntegerField(default=0 max_value=5 min_value=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('movies:detail', kwargs={'id': self.pk})

class Comment(models.Model)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    comment = models.TextField(blank=True, null=True max_length=3000)

    

