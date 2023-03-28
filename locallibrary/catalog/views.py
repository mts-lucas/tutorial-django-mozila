from catalog.models import Author, Book, BookInstance, Genre  # noqa: F401
from django.shortcuts import render
from django.views import generic

# Create your views here.


def index(request):

    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    num_instances_available = BookInstance.objects.filter(
        status__exact='a').count()

    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
    }

    return render(request, 'index.html', context=context)


class BookListView(generic.ListView):
    model = Book
    paginate_by = 10
    template_name = 'book_list.html'


class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'book_detail.html'
