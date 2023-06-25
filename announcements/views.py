from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author':'niv',
        'title': 'post1',
        'content': 'first content',
        'date_posted': 'june 6,2023',
    },{
        'author':'jomar',
        'title': 'post2',
        'content': 'second content',
        'date_posted': 'june 8,2023',
    }
]
def home(request):
    context = {
        'posts' : posts
    }
    return render(request, 'announcements/home.html',context)

def about(request):
    return render(request, 'announcements/about.html', {'title':'hello'})