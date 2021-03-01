from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .models import Post

# Create your views here.

#Home view - index.html
def home(request):
    posts = Post.objects.filter(status='published')
    context = {"posts":posts}
    return render(request, "post/index.html", context)


#For post details
def detail(request, pk, slug):
    post = get_object_or_404(Post, id=pk, slug=slug)
    context = {"post":post}
    return render(request, "post/details.html", context)


#Create new blog-post
def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        slug = request.POST.get('slug')
        detail = request.POST.get('detail')
        status = request.POST.get('status')

        if title and detail:
            p = Post.objects.create(title=title, slug=slug, detail=detail, status=status, author=request.user)
            return redirect(p.get_absolute_url())
    return render(request, "post/create.html")

    
#Edit blog-post
def edit(request, pk, slug):
    post = get_object_or_404(Post, id=pk, slug=slug)
    context = {'post':post}
    if request.method == "POST":
        title = request.POST.get('title')
        detail = request.POST.get('detail')
        status = request.POST.get('status')

        if title and detail:
            post.title=title
            post.detail=detail
            post.status=status
            post.save()
            return redirect(post.get_absolute_url())
        
    return render(request, "post/edit.html", context)


#Delete blog-post (Admins only)
def delete(request, pk, slug):
    post = get_object_or_404(Post, id=pk, slug=slug)
    context = {'post':post}
    if request.method == "POST":
        post.delete()
        return redirect("post:home")
        
    return render(request, "post/delete.html", context)

