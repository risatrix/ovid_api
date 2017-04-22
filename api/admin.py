# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from api.models import Author, Work, Book, Poem, Line

# Register your models here.
admin.site.register(Author)
admin.site.register(Work)
admin.site.register(Book)
admin.site.register(Poem)
admin.site.register(Line)
