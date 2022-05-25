from unittest import loader
from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Movie, Cast, Director, Genre
from rest_framework import viewsets
from .serializers import CastSerializer, MovieSerializer, DirectorSerializer, GenreSerializer, MainSeializer
from rest_framework import filters


class CastViewSet(viewsets.ModelViewSet):
    queryset = Cast.objects.all()
    serializer_class = CastSerializer

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MainSeializer
    
    def get_queryset(self):
        queryset = super(MovieViewSet, self).get_queryset()
        cast_name = self.request.query_params.get('cast_name', None)
        director_name = self.request.query_params.get('director_name', None)
        genre_name = self.request.query_params.get('genre_name', None)
        
        if cast_name:
            queryset = queryset.filter(cast__name=cast_name)
        if director_name:
            queryset = queryset.filter(director__name=director_name)
        if genre_name:
            queryset = queryset.filter(genre__name=genre_name)

        return queryset

class DirectorViewSet(viewsets.ModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

