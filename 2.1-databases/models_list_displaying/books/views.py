from datetime import datetime

from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render

from books.models import Book


def books_view(request):
    template = 'books/books_list.html'
    books_objects = Book.objects.all()
    context = {
        'books': books_objects
    }
    return render(request, template, context)


def books_add(request):
    """
    example
    http://127.0.0.1:8000/add/?name=Метро-2035&author=Дмитрий-Глуховский&pub_date=2015-06-15
    """
    name = request.GET.get('name')
    author = request.GET.get('author')
    date = request.GET.get('pub_date')
    pub_date = datetime.strptime(date, '%Y-%m-%d')
    book = Book(name=name.replace('-', ' '), author=author.replace('-', ' '), pub_date=pub_date)
    book.save()
    return HttpResponse(f'Добавлена книга: <br> {book.name}, {book.author}, {book.pub_date}')


def books_date_view(request, dt: datetime):
    template = 'books/book.html'
    book_object = Book.objects.filter(pub_date=dt)
    pages_list = [f'{x.pub_date}' for x in Book.objects.order_by('pub_date')]
    p = 0
    for i, date_ in enumerate(pages_list):
        if date_ == f'{datetime.date(dt)}':
            p = i
    paginator = Paginator(pages_list, 1)
    page = paginator.get_page(p+1)
    if p+1 >= len(pages_list):
        pages_n = None
    else:
        pages_n = pages_list[p+1]
    if p == 0:
        pages_p = None
    else:
        pages_p = pages_list[p-1]
    context = {
        'books': book_object,
        'page': page,
        'pages_p': pages_p,
        'pages_n': pages_n,
    }
    return render(request, template, context)
