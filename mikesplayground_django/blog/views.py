from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost
from django.http import Http404
from .forms import BlogPostForm
from datetime import datetime
from django.contrib.auth.models import User


# Create your views here.
def database_view(request, *args, **kwargs):
    context = {}
    return render(request, "imperial_library.html", context)


def blogpost_list_view(request):
    queryset = BlogPost.objects.all()
    context = {"object_list": queryset}
    return render(request, "blogpost_list.html", context)


def dynamic_lookup_view(request, id):
    try:
        obj = BlogPost.objects.get(id=id)
    except BlogPost.DoesNotExist:
        raise Http404
    context = {'object': obj}
    return render(request, "blogpost_detail.html", context)


def blogpost_delete_view(request, id):
    obj = get_object_or_404(BlogPost, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../')
    context = {'object': obj}
    return render(request, "blogpost_delete.html", context)


def blogpost_edit_view(request, id):
    obj = BlogPost.objects.get(id=id)
    initial_data = {
        'title': obj.title,
        'content': obj.content,
        'author': obj.author,
        'date': obj.date
    }
    form = BlogPostForm(request.POST or None, initial=initial_data, instance=obj)
    if form.is_valid():
        form.save()
        # form = BlogPostForm()
        return redirect('../../')

    context = {'form': form}
    return render(request, "blogpost_create.html", context)

        
def blogpost_create_view(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('../')
        else:
            print("Form invalid")
    else:
        initial_data = {'date': datetime.now(), 'author': request.user.get_username()}
        form = BlogPostForm(request.POST or None, initial=initial_data)
        context = {'form': form}
        return render(request, "blogpost_create.html", context)
