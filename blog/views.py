from django.shortcuts import render

from blog.models import Blog

# Create your views here.
def blogs(request):
    blogs = Blog.objects.all().order_by('-date')
    return render(request, 'blog/blogs.html', {'blogs': blogs})


def blog_post(request, url_title):
    blog = Blog.objects.get(url_title=url_title)
    return render(request, 'blog/blog.html', {'blog': blog})
