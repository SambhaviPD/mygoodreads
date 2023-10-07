import os

import django
from pytest_factoryboy import register

from .factories import BookFactory

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mybookshelf.settings.local")
django.setup()

register(BookFactory)
