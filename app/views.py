from django.contrib.auth.models import User
from rest_framework import viewsets
from app.models import Author, Book, HeadOffice, Collaborator, HeadOfficeBook
from app.serializers import AuthorSerializer, BookSerializer, HeadOfficeSerializer, CollaboratorSerializer, \
    UserSerializer, HeadOfficeBookSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    """
    List of book authors
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):
    """
    Books submitted
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class HeadOfficeViewSet(viewsets.ModelViewSet):
    """
    Headoffices
    """
    queryset = HeadOffice.objects.all()
    serializer_class = HeadOfficeSerializer


class CollaboratorViewSet(viewsets.ModelViewSet):
    """
    Collaborators
    """
    queryset = Collaborator.objects.all()
    serializer_class = CollaboratorSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    Users in the system
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class HeadOfficeBookViewSet(viewsets.ModelViewSet):
    """
    Shows total and availables copys of a book in a determined head office
    """
    queryset = HeadOfficeBook.objects.all()
    serializer_class = HeadOfficeBookSerializer

