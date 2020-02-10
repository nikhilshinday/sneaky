from django.shortcuts import render

from blog.models import Blog, Book


def index(request):
    blogs = Blog.objects.all().order_by('date').values('title', 'url_title')[:3]
    books = Book.objects.all().order_by('date_ts')[:3]
    return render(
        request,
        'sneaky/index.html',
        {
            'blogs': blogs,
            'books': books
        }
    )
