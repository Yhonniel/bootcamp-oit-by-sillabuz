from rest_framework import serializers

from library.models import Author, Book


class AuthorSerializers(serializers.ModelSerializer):
    # id en read_only por que es un dato que se genera en la BD
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)

    class Meta:
        model = Author
        fields = ('id', 'name')


class BookSerializers(serializers.ModelSerializer):
    # id en read_only por que es un dato que se genera en la BD
    id = serializers.IntegerField(read_only=True, )
    author = AuthorSerializers()
    name = serializers.CharField(required=True, )
    publication_date = serializers.DateField()

    class Meta:
        model = Book
        fields = ('id', 'name', 'author', 'publication_date')
