from rest_framework import serializers
from django.contrib.auth.models import User
from app.models import Author, Book, HeadOffice, Collaborator, HeadOfficeBook


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class HeadOfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeadOffice
        fields = '__all__'


class CollaboratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collaborator
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password']
        # fields = '__all__'

class HeadOfficeBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeadOfficeBook
        fields = '__all__'
