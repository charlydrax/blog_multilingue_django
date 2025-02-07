from django.shortcuts import render, get_object_or_404
from .models import Post

#Home page
def home(request):
    return render(request, 'home.html')

# Vue pour afficher la liste des articles
def post_list(request):
    posts = Post.objects.filter(status=1).order_by('created_on')
    return render(request, 'blog.html', {'posts': posts})

# Vue pour afficher les détails d'un article
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_details.html', {'post': post})