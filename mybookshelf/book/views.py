from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from .models import Book


# Create your views here.
class HomeView(ListView):
    model = Book
    template_name = "book/index.html"


class BookListView(LoginRequiredMixin, ListView):
    model = Book
    template_name = "book/book_list.html"
