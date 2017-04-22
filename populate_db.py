import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ovid_api.settings')

import django
django.setup()

import json
from api.models import Author, Work, Book, Poem, Line


json_data = open('corpus.json')
data = json.load(json_data)
author = data['author']
works = data['works']

# clear the decks so there are no conflicts
Author.objects.all().delete()
Work.objects.all().delete()
Book.objects.all().delete()
Poem.objects.all().delete()
Line.objects.all().delete()

# start with the author. There's only one to worry about for now.
def add_author(name, full_name, abbreviation, slug):
    a = Author.objects.create()
    a.name = name
    a.full_name = full_name
    a.abbreviation = abbreviation
    a.slug = slug
    a.save()
    return a

name = author[0]['name']
slug = author[1]['slug']
full_name = author[2]['full name']
abbreviation = author[3]['abbreviation']


add_author(name=name, full_name=full_name, abbreviation=abbreviation, slug=slug)

ovid = Author.objects.get(name="Ovid")

# loop through the JSON and create database objects as we go
for idx, work in enumerate(works, start=0):
    w = Work()
    w.title = works[idx]["title"]
    w.abbreviation = works[idx]["abbreviation"]
    w.slug = works[idx]["slug"]
    w.author = ovid
    books = works[idx]["books"]
    w.save()
    for book in books:
        b = Book()
        b.book_index = book['book_index']
        b.title = book['book_title']
        b.work = w
        b.save()
        poems = book["poems"]
        for poem in poems:
            p = Poem()
            p.poem_index = poem['poem_index']
            p.title = poem['poem_title']
            p.book = b
            p.save()
            lines = poem['lines']
            for line in lines:
                print line['text']
                print line['line_index']
                l = Line()
                l.text = line['text']
                l.meter = line['meter']
                l.line_index = line['line_index']
                l.poem = p
                l.save()

json_data.close()

