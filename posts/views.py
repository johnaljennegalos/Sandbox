from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
def post_list(request):
    posts = Post.objects.all().order_by('-date')
    return render(request, 'posts/posts_list.html', {'posts': posts})

def post_page(request, slug):
    return HttpResponse(slug)

