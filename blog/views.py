from django.shortcuts import render

# Create your views here.
posts = [
    {
        "author":"Lashley",
        "title":"Beat up LANA",
        "content": "Lana had a little lamp",
        "date_posted": "2018"
    },
    {
        "author":"Lashley",
        "title":"Beat up Rusev",
        "content": "Lana had a little dump",
        "date_posted": "2018"
    },
]
def home(req):
    context = {
        'posts': posts,
        'title': 'home'
    }
    return render(req, 'blog/home.html', context)


def about(req):
    return render(req, 'blog/about.html')