import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ovid_api.settings')

import django
django.setup()

import json
from api.models import Author


json_data = open('corpus.json')
data = json.load(json_data)
author = data['author']
works = data['works']

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

add_author(name=name, full_name=full_name, abbrev=abbreviation, slug=slug)

json_data.close()
