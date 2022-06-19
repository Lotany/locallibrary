from django.shortcuts import render

# Create your views here.
from .models import Book, Author, BookInstance, Genre

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_genre=Genre.objects.count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_genre':num_genre,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
from django.views import generic

class BookListView(generic.ListView):
        model=Book
        paginate_by=10
       # context_object_name='book_list' #variable
        #queryset=Book.objects.filter(title_icontains='war')[:5] #get 5 books containing title war
       # template_name='books/book_list.html' #specify your own name

class BookDetailView(generic.DetailView):
    model=Book


class AuthorListView(generic.ListView):
    model=Author

class AuthorDetailView(generic.DetailView):
    model=Author

