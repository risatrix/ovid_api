# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404

from api.models import Author, Work, Book, Poem, Line
from api.serializers import AuthorSerializer, BookSerializer, LineSerializer, WorkSerializer, PoemSerializer

from rest_framework import viewsets
from rest_framework.response import Response


def index(request):
     context_dict = {}
     return render(request, 'ovid_api/index.html', context=context_dict)


class AuthorViewSet(viewsets.ViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    lookup_field = 'slug'

    def list(self, request):
        queryset = Author.objects.filter()
        serializer = AuthorSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, slug=None):
        queryset=Author.objects.filter()
        # author= get_object_or_404(queryset, author__slug=slug)
        author = Author.objects.get(slug = self.kwargs['slug'])
        serializer = AuthorSerializer(author)
        return Response(serializer.data)


class WorkViewSet(viewsets.ViewSet):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
    lookup_field = 'slug'

    def list(self, request, author_slug=None):
        queryset = Work.objects.filter(author__slug=author_slug)
        serializer = WorkSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, slug=None, author_slug=None):
        queryset = Work.objects.filter(slug=slug,author__slug=author_slug)
        work = get_object_or_404(queryset, slug=slug)
        serializer = WorkSerializer(work)
        return Response(serializer.data)


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'book_index'

    def list(self, request, author_slug=None, work_slug=None):
        queryset = Book.objects.filter(work__author__slug = author_slug, work__slug=work_slug)
        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, book_index=None, author_slug=None, work_slug=None):
        queryset = Book.objects.filter(book_index=book_index,work__slug=work_slug, work__author__slug=author_slug)
        book = get_object_or_404(queryset, book_index=book_index)
        serializer = BookSerializer(book)
        return Response(serializer.data)


class PoemViewSet(viewsets.ModelViewSet):
    queryset = Poem.objects.all()
    serializer_class = PoemSerializer
    lookup_field = 'poem_index'

    def list(self, request, book_book_index=None, author_slug=None, work_slug=None):
        work = Work.objects.filter(slug=work_slug)
        queryset=Poem.objects.filter(book__book_index=book_book_index, book__work=work)
        serializer = PoemSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, poem_index=None, book_book_index=None, author_slug=None, work_slug=None):
        work = Work.objects.filter(slug=work_slug)
        queryset = Poem.objects.filter(book__book_index=book_book_index, book__work=work)
        poem = get_object_or_404(queryset, poem_index=poem_index)
        serializer = PoemSerializer(poem)
        return Response(serializer.data)


class LineViewSet(viewsets.ModelViewSet):
    queryset = Line.objects.all()
    serializer_class = LineSerializer
    lookup_field = 'line_index'

    def list(self, request, poem_poem_index=None, book_book_index=None, author_slug=None, work_slug=None):
        work = Work.objects.filter(slug=work_slug)
        queryset=Line.objects.filter(poem__poem_index=poem_poem_index,
            poem__book__book_index=book_book_index, poem__book__work=work)
        serializer = LineSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, line_index=None, poem_poem_index=None, book_book_index=None, author_slug=None, work_slug=None):
        work = Work.objects.filter(slug=work_slug)
        queryset = Line.objects.filter(line_index=line_index,
            poem__poem_index=poem_poem_index, poem__book__book_index=book_book_index, poem__book__work=work)
        line = get_object_or_404(queryset, poem__poem_index=poem_poem_index)
        serializer = LineSerializer(line)
        return Response(serializer.data)
