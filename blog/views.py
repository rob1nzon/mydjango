from django.shortcuts import render
from blog.models import Post
     
def index(request):
# get the blog posts that are published
 posts = Post.objects.filter(published=True)
 mainp = Post.objects.filter(main=True)
# now return the rendered template
 return render(request, 'blog/index.html', {'posts': posts,'mainp': mainp})
     
def post(request, slug):
# get the Post object
 post = get_object_or_404(Post, slug=slug)
 # now return the rendered template
 return render(request, 'blog/post.html', {'post': post})

#def mainp(request):
# mainp = Post.objects.filter(main=True)
# return render(request, 'blog/m.html',{'mainp':mainp})


