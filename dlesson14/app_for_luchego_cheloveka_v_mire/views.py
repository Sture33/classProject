from django.shortcuts import render, redirect
from .form import Blog_form
from .models import Blog


# Create your views here.
def index(request):
    context = {'feedback_list': Blog.objects.all()}
    return render(request, 'index.html', context)

def form(request):
    context = {}
    if request.method == 'POST':
        form = Blog_form(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            title = form.cleaned_data['title']
            text = form.cleaned_data['text']
            quantity_of_likes = form.cleaned_data['quantity_of_likes']
            blog = Blog()
            blog.name = name
            blog.title = title
            blog.text = text
            blog.quantity_of_likes = quantity_of_likes
            blog.save()
            return redirect('index')
        else:
            print( 'Invalid')
    form = Blog_form()
    context['form'] = form
    return render(request, 'form.html', context)

def detail(request, pk):
    context = {'detail': Blog.objects.get(pk=pk)}
    return render(request,'detail.html', context)