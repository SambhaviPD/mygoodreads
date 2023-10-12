from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.decorators.http import require_http_methods
from django.views.generic import CreateView, ListView

from .forms import CustomUserCreationForm
from .models import Book


# Create your views here.
class HomeView(ListView):
    model = Book
    template_name = "book/index.html"


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("book:login")
        else:
            form = CustomUserCreationForm()
    return render(
        request, "registration/register.html", {"form": CustomUserCreationForm}
    )


class BookListView(LoginRequiredMixin, ListView):
    model = Book
    template_name = "book/book_list.html"
    context_object_name = "books"
    paginate_by = 10

    def get_queryset(self):
        return Book.objects.filter(created_by=self.request.user)


class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    template_name = "book/book_create.html"
    fields = ["title", "author", "description", "cover", "status"]

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.updated_by = self.request.user
        return super().form_valid(form)

    def get_success_url(self) -> str:
        return reverse_lazy("book:book-list")


@require_http_methods(["DELETE"])
def delete_book(request, pk):
    Book.objects.filter(pk=pk).delete()
    # books = Book.objects.filter(created_by=request.user)
    return HttpResponse()


@require_http_methods(["GET", "POST"])
def quick_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        print("book = ", book)
        book.title = request.POST.get("title", "").strip()
        book.author = request.POST.get("author", "").strip()
        print("book.title = ", book.title)
        print("book.author = ", book.author)
        book.save()
        return render(request, "book/partials/book.html", {"book": book})
    return render(request, "book/partials/edit.html", {"book": book})


@require_http_methods(["GET"])
def render_quick_edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, "book/_book_row.html", {"book": book})
