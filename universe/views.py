from django.shortcuts import render
from universe.models import Post


# Create your views here.

def main_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')


def posts_view(request):
    if request.method == 'GET':
        posts = Post.objects.all()

        context_data = {
            'posts': posts
        }

        return render(request, 'posts/index.html', context=context_data)


def products_view(request):
    if request.method == 'GET':
        products = Post.objects.all()

        products_data = {
            'products': products
        }
    return render(request, "products/products.html", {"products": products_data})

