# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404

from api.models import Author, Work, Book, Poem, Line
from api.serializers import AuthorSerializer, BookSerializer, LineSerializer, WorkSerializer, PoemSerializer

from rest_framework import viewsets
from rest_framework.response import Response

class AuthorViewSet(viewsets.ViewSet):
    queryset = Author.objects.all()

    serializer_class = AuthorSerializer

    def list(self, request):
        queryset = Author.objects.filter()
        serializer = AuthorSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset=Author.objects.filter()
        author= get_object_or_404(queryset, pk=pk)
        serializer = AuthorSerializer(author)
        return Response(serializer.data)


class WorkViewSet(viewsets.ViewSet):
    queryset = Work.objects.all()

    serializer_class = WorkSerializer

    def list(self, request, author_pk=None):
        queryset = Work.objects.filter(author=author_pk)
        serializer = WorkSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, author_pk=None):
        queryset = Work.objects.filter(pk=pk,author=author_pk)
        work = get_object_or_404(queryset, pk=pk)
        serializer = WorkSerializer(work)
        return Response(serializer.data)

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class LineViewSet(viewsets.ModelViewSet):
    queryset = Line.objects.all()[10:]
    serializer_class = LineSerializer

class PoemViewSet(viewsets.ModelViewSet):
    queryset = Poem.objects.all()[1:]
    serializer_class = PoemSerializer

