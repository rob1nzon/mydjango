from django.shortcuts import render,get_object_or_404
from blog.models import Post
     
def index(request):
# get the blog posts that are published
 posts = Post.objects.filter(published=True)
 mainp = Post.objects.filter(main=True)
# now return the rendered template
 return render(request, 'blog/index.html', {'posts': posts,'mainp': mainp})
     
def post(request, slug):
# get the Post object
 if True:
  post = get_object_or_404(Post, slug=slug)
  menu = Post.objects.filter(published=True)
 # now return the rendered template
 return render(request, 'blog/post.html', {'post': post, 'menu':menu})

#def mainp(request):
# mainp = Post.objects.filter(main=True)
# return render(request, 'blog/m.html',{'mainp':mainp})


