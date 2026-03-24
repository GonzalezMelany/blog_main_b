from django.db.models import Q
from django.shortcuts import render, get_object_or_404, render

from.models import Post, Category

# Create your viws here
def home(request):
    post = Post.objects.filter(status=Post.ACTIVE).order_by('-created_at')
    context = {
        'post': post
        
    }
    return render(request,'blog/home.html',context)