from django.shortcuts import render
from django.http import HttpResponse
from my_blog.models import Blog
from datetime import datetime

# Create your views here.
def home(request):
    post_list = Blog.objects.all()  # 获取全部Blog对象
    return render(request, 'home.html', {'post_list':post_list})

def detail(request, my_args):
    post = Blog.objects.all()[int(my_args)]
    str = ("title=%s, category=%s, date_time=%s, content=%s"
           % (post.title, post.category, post.date_time, post.content))
    return HttpResponse(str)