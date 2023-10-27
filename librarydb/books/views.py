from django.shortcuts import render
from django.views.generic import ListView
from .models import Books
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DetailView
from django.views.generic import DeleteView
from django.urls import reverse_lazy # Neu
# Create your views here.

class FavBook(ListView):
    model = Books
    template_name = 'books/book_home.html'

class BookCreate(CreateView):
    model = Books
    template_name = 'books/books_create.html'
    fields = '__all__'
    success_url = reverse_lazy('book_start')
class BookDetail(DetailView):
    model = Books
    template_name = 'books/books_detail.html'
class BookUpdate(UpdateView):
    model = Books
    template_name = 'books/books_update.html'
    fields = '__all__'
class BookDelete(DeleteView):
    model = Books
    template_name = "books/books_delete.html"
    fields = '__all__'
    success_url = reverse_lazy('book_start')

    