from django.db import models
from django.urls import reverse
import uuid #unique book instance

# Create your models here.

#model representing a book genre
class Genre(models.Model):
    name=models.CharField(max_length=200, help_text='Enter a book genre(eg science fiction)')
    
     #string for representing model object
    def _str_(self):
        return self.name


#model representing a book but not a specific copy of a book
#Foreign key used because book can have only one author
#author as a string because it hasnt beeen declared yet

class Book(models.Model):
    title=models.CharField(max_length=200)
    author=models.ForeignKey('Author',on_delete=models.SET_NULL,null=True)
    summary=models.TextField(max_length=1000,help_text='Enter a brief description of the book')
    isbn=models.CharField('ISBN',max_length=13,unique=True,help_text='13 character<a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')

    #many to many relationship because genre can contain many books and books can have many gnres
    genre=models.ManyToManyField(Genre,help_text='select a genre for this book')

   #string for representing the model
    def _str_(self):
        return self.title

#returns the url to access a detail record for this book
    def get_absolute_url(self):
        return reverse ('book-detail',args=[str(self.id)])


#model representing a specific set of book that can be borrowed from the library

class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,help_text='Unique id for this particular book accross whole library')
    book=models.ForeignKey('Book',on_delete=models.RESTRICT,null=True)
    imprint=models.CharField(max_length=200)
    due_back=models.DateField(null=True,blank=True)
    LOAN_STATUS=(
        ('m','Maintenance'),
        ('o','On loan'),
        ('a','Available'),
        ('r','Reserved'),
        )

    status=models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,default='m',
        help_text='Book Availability',
        )

class Meta:
    ordering=['due_back']

    def _str_(self):
        return f'{self.id}({self.book.title})'

#model representinf author
class Author(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    date_of_birth=models.DateField(null=True,blank=True)
    date_of_death=models.DateField('Died',null=True,blank=True)

class Meta:
    ordering=['last_name','first_name']


    def get_absolute_url(self):
        return reverse('author-detail',args=[str(self.id)])

    def _str_(self):
        return f'{self.last_name},{self.last_name}'
