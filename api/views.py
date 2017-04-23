# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from api.models import Author, Work, Book, Poem, Line
from rest_framework import viewsets
from api.serializers import AuthorSerializer, BookSerializer, LineSerializer, WorkSerializer, PoemSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class LineViewSet(viewsets.ModelViewSet):
    queryset = Line.objects.all()[10:]
    serializer_class = LineSerializer

class PoemViewSet(viewsets.ModelViewSet):
    queryset = Poem.objects.all()[1:]
    serializer_class = PoemSerializer

class WorkViewSet(viewsets.ModelViewSet):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
