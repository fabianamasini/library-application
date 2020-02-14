from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=100)
    publication_date = models.DateField()
    number_of_pages = models.IntegerField()
    bar_code = models.CharField(max_length=500)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='book_cover/', default='book_cover/no-img.jpg')

    def __str__(self):
        return self.name


class HeadOffice(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class HeadOfficeBook(models.Model):
    book = models.OneToOneField(Book, on_delete=models.CASCADE)
    head_office = models.OneToOneField(HeadOffice, on_delete=models.CASCADE)
    total = models.IntegerField(default=0)
    available = models.IntegerField(default=0)


class Collaborator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cpf = models.CharField(max_length=11, unique=True, blank=False, null=False)
    head_office = models.ForeignKey(HeadOffice, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

