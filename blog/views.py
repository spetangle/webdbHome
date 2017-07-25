from django.shortcuts import render
from blog.models import BlogsPost
from django.shortcuts import render_to_response
from django.forms.models import model_to_dict


# Create your views here.

def index(request):
    blog_list = BlogsPost.objects.all()
    return render_to_response('index.html', {'blog_list': blog_list})


def content(request,postid):
    post = model_to_dict(BlogsPost.objects.get(id=postid))
    print(post)
    return render(request,'showpost.html', {'post':post})


