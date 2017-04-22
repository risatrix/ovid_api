from api.models import Author, Work, Book, Poem, Line
from rest_framework import serializers


class LineSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Line
        fields = ('text', 'meter', 'line_index')

class WorkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Work
        fields = ('title', 'abbreviation')

