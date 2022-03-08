from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
posts = [
    {
        'author': 'Rachan',
        'title': 'blog post 1',
        'content': 'first post',
        'date_posted': 'feb 24 2022 '
    },

    {
        'author': 'sujan',
        'title': 'blog post 2',
        'content': 'second post',
        'date_posted': 'feb 25 2022'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):

    return render(request, 'blog/about.html', {'title': ' Aboutt'})
