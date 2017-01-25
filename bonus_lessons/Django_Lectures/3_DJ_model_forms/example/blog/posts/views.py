from django.shortcuts import render, get_object_or_404
from django import forms
from .models import Post
from posts.forms import PostForm

def posts_detail(req, id=None):

    post = get_object_or_404(Post, id=id)
    mf = PostForm()
    print(mf)
    context = {
        "post": mf,
    }
    return render(req, "detail_view.html", context)