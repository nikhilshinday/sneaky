from django.shortcuts import render

from blog.models import Blog


def index(request):
    blogs = Blog.objects.all().order_by('date').values('title', 'url_title')
    return render(
        request,
        'sneaky/index.html',
        {
            'blogs': blogs
        }
    )
