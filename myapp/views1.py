
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Publisher, Book

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
    response = HttpResponse()
    title = f'<p>Title: {book.title.upper()}</p>'
    price = f'<p>Price: ${book.price}</p>'
    publisher = f'<p>Publisher: {book.publisher.name}</p>'
    response.write(title)
    response.write(price)
    response.write(publisher)
    return render(request, 'myapp/detail.html', {'book': book})
