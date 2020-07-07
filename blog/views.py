from django.shortcuts import render, get_object_or_404
from .models import Blog
# Create your views here.

# PAGE FOR THE BLOG
def all_blogs(request):

    blogs = Blog.objects.order_by('-date_post')
    return render(request,'blog/all_blogs.html',{'blogs':blogs})


# ANOTHER PAGE FOR MORE DETAILS OF THE BLOG
def details(request, blog_id):

    # GETTING THE PRIMARY KEY
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request,'blog/detail.html',{'blog':blog})
