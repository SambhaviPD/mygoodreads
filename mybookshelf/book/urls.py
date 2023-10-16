from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

app_name = "book"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("register/", views.register, name="register"),
    path("book-list", views.BookListView.as_view(), name="book-list"),
    path("book-create", views.BookCreateView.as_view(), name="book-create"),
    path(
        "books/<int:pk>/delete",
        views.delete_book,
        name="book-delete",
    ),
    path(
        "books/<int:pk>/quickedit",
        views.quick_edit,
        name="quick-edit",
    ),
    path("search/", views.search, name="search"),
]
