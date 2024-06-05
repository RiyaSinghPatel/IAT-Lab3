# Import necessary classes
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Publisher, Book, Member, Order

# Create your views here.
def index(request):
    response = HttpResponse()

    # Retrieve books ordered by primary key
    booklist = Book.objects.all().order_by('id')

    # Display list of books
    heading1 = '<p>' + 'List of available books: ' + '</p>'
    response.write(heading1)
    for book in booklist:
        para = '<p>' + str(book.id) + ': ' + str(book) + '</p>'
        response.write(para)

    # Retrieve publishers ordered by city name in descending order
    publishers = Publisher.objects.all().order_by('-city')

    # Display list of publishers
    heading2 = '<p>' + 'List of Publishers: ' + '</p>'
    response.write(heading2)
    for publisher in publishers:
        para = '<p>' + str(publisher.name) + ', ' + str(publisher.city) + '</p>'
        response.write(para)

    return response


def about(request):
    return render(request, 'myapp/about.html')

def detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    context = {
        'book': book,
    }
    return render(request, 'myapp/detail.html', context)
