from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Book(models.Model):
    options = (
        ("read", "Read"),
        ("reading", "Reading"),
        ("want to read", "Want to Read"),
    )

    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = models.TextField()
    cover = models.ImageField(upload_to="covers/", blank=True)
    status = models.CharField(
        max_length=30, choices=options, default="want to read"
    )
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="books_createdby"
    )
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="books_updatedby"
    )
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return self.title
