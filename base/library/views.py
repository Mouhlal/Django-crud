from django.shortcuts import render , redirect
from django.views import View
from django.http import HttpResponse
from .models import Author, Book
from django.urls import path
from .forms import AuthorForm  , BookForm

# Create your views here.

class Home(View):
    def get(self, request):
        return HttpResponse("Hello, world. You're at the library index.")

class AuthorList(View):
    def get(self , request):
        authors = Author.objects.all()
        books = Book.objects.all()
        return render(request, 'home.html', {'authors': authors , 'books': books})

class AddAuthor(View):
    def get(self, request):
        form = AuthorForm()
        return render(request, 'create.html', {'form': form})

    def post(self, request):
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('author_list') 
        return render(request, 'create.html', {'form': form})

class DeleteAuthor(View):
    def get(self,request,id):
        Author.objects.filter(id=id).delete()
        return redirect('author_list')

class UpdateAuthor(View):
    def get(self, request, id):
        author = Author.objects.get(id=id)
        form = AuthorForm(instance=author)
        return render(request, 'update.html', {'form': form})

    def post(self, request, id):
        author = Author.objects.get(id=id)
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect('author_list')
        return render(request, 'update.html', {'form': form})  

