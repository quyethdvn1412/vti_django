from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Book, BookForm, AuthorForm
# Create your views here.

def index(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("<h2> Data save successful! </h2>")
        else:
            return HttpResponse("<h2> Data save not successful! </h2>")
    form = AuthorForm()
    return render(request, 'authors.html', {'form': form})


# def index(request):
#     if request.method == 'POST':
#         a = Author.objects.get(pk=2)
#         f = AuthorForm(request.POST, instance=a)
#         if f.is_valid():
#             f.save()
#             return HttpResponse("<h2> Data save successful! </h2>")
#         else:
#             return HttpResponse("<h2> Data save not successful! </h2>")
#     form = AuthorForm()
#     return render(request, 'authors.html', {'form': form})