from api.models import Author, Work, Book, Poem, Line
from rest_framework import serializers


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    works = serializers.StringRelatedField(many=True)

    class Meta:
        model = Author
        fields = ('name', 'full_name', 'works', 'slug')
        lookup_field = 'slug'

class WorkSerializer(serializers.HyperlinkedModelSerializer):
    books = serializers.StringRelatedField(many=True)

    class Meta:
        model = Work
        fields = ('title', 'abbreviation', 'books', 'slug')
        lookup_field = 'slug'


class BookSerializer(serializers.HyperlinkedModelSerializer):
    poems = serializers.StringRelatedField(many=True)

    class Meta:
        model = Book
        fields = ('title', 'poems')
        lookup_field = 'book_index'

class LineSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Line
        fields = ('text', 'meter', 'line_index')

class PoemSerializer(serializers.HyperlinkedModelSerializer):
    lines = serializers.StringRelatedField(many=True)

    class Meta:
        model = Poem
        fields = ('title', 'lines')




