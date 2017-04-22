# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from api.models import Author, Work, Book, Poem, Line
from rest_framework import viewsets
from api.serializers import LineSerializer, WorkSerializer, PoemSerializer


class LineViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Line.objects.all()[10:]
    serializer_class = LineSerializer


class WorkViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Work.objects.all()
    serializer_class = WorkSerializer

class PoemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Poem.objects.all()[1:]
    serializer_class = PoemSerializer
