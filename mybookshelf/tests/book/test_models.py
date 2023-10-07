import pytest

pytestmark = pytest.mark.django_db


class TestBookModel:
    def test_str_return(self, book_factory):
        book = book_factory(title="Test Book")
        assert book.__str__() == "Test Book"
