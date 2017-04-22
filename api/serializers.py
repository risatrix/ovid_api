from api.models import Author, Work, Book, Poem, Line
from rest_framework import serializers


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    works = serializers.StringRelatedField(many=True)
    class Meta:
        model = Author
        fields = ('name', 'full_name', 'works')

class LineSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Line
        fields = ('text', 'meter', 'line_index')

class WorkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Work
        fields = ('title', 'abbreviation')

class PoemSerializer(serializers.HyperlinkedModelSerializer):
    lines = serializers.StringRelatedField(many=True)
    class Meta:
        model = Poem
        fields = ('title', 'lines')

