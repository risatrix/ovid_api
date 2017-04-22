# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=128, unique=True)
    full_name = models.CharField(max_length=128, unique=True)
    abbreviation = models.CharField(max_length=128, unique=True)
    slug = models.CharField(max_length=128, unique=True)

    def __unicode__(self):
        return self.name

class Work(models.Model):
    title = models.CharField(max_length=128, unique=True)
    abbreviation = models.CharField(max_length=128, unique=True)
    slug = models.CharField(max_length=128, unique=True)
    author = models.ForeignKey(Author, blank=True, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.title

class Book(models.Model):
    title = models.CharField(max_length=128)
    book_index = models.IntegerField()
    work = models.ForeignKey(Work, blank=True, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.title

class Poem(models.Model):
    title = models.CharField(max_length=128)
    poem_index = models.IntegerField()
    book = models.ForeignKey(Book, blank=True, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.title

class Line(models.Model):
    line_index = models.IntegerField()
    text = models.CharField(max_length=500, unique=True)
    meter = models.CharField(max_length=128, unique=True)
    poem = models.ForeignKey(Poem, blank=True, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.text
