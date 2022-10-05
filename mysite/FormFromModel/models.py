from django.db import models
from django.forms import ModelForm
TITLE_CHOICE = (
    ('MR', 'Mr.'),
    ('MRS', 'Mrs.'),
    ('MS', 'Ms.'),
)
# Create your models here.
class Author(models.Model):
    author_name = models.CharField(max_length=100)
    title = models.CharField(max_length=3, choices=TITLE_CHOICE)
    birth_date = models.DateField()
class Book(models.Model):
    book_name = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['author_name', 'title', 'birth_date']
class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['book_name', 'authors']