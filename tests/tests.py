import sys
import unittest as tester

sys.path.append('../src')
sys.path.append('../src/enum')

from Enums import Order, Type
from BookSorter import BookSorter, SortingServiceException




book1 = {
    'title': 'Java How to Program',
    'author': 'Deitel & Deitel',
    'edition_year': 2007
    }

book2 = {
    'title': 'Patterns of Enterprise Application Architecture',
    'author': 'Martin Fowler',
    'edition_year': 2002
    }

book3 = {
    'title': 'Head First Design Patterns',
    'author': 'Elisabeth Freeman',
    'edition_year': 2004
    }

book4 = {
    'title': 'Internet & World Wide Web: How to Program',
    'author': 'Deitel & Deitel',
    'edition_year': 2007
    }

bookshelf = [book1, book2, book3, book4]


class BookSorterTester(tester.TestCase):

    def test_title_ordering_ascending(self):
        rules = [(Type.title, Order.ascending)]
        expected = [book3, book4, book1, book2]

        book_sorter = BookSorter()
        result = book_sorter.sort_books(bookshelf, rules)

        self.assertEqual(expected, result)

    def test_title_ordering_descending(self):
        rules = [(Type.title, Order.descending)]
        expected = [book2, book1, book4, book3]

        book_sorter = BookSorter()
        result = book_sorter.sort_books(bookshelf, rules)

        self.assertEqual(expected, result)

    def test_author_ordering_ascending(self):
        rules = [(Type.author, Order.ascending)]
        expected = [book1, book4, book3, book2]

        book_sorter = BookSorter()
        result = book_sorter.sort_books(bookshelf, rules)

        self.assertEqual(expected, result)

    def test_author_ordering_descending(self):
        rules = [(Type.author, Order.descending)]
        expected = [book2, book3, book1, book4]

        book_sorter = BookSorter()
        result = book_sorter.sort_books(bookshelf, rules)

        self.assertEqual(expected, result)

    def test_title_ordering_ascending_author_ordering_ascending(self):
        rules = [(Type.title, Order.ascending), (Type.author, Order.ascending)]
        expected = [book3, book4, book1, book2]

        book_sorter = BookSorter()
        result = book_sorter.sort_books(bookshelf, rules)

        self.assertEqual(expected, result)

    def test_title_ordering_ascending_author_ordering_descending(self):
        rules = [(Type.title, Order.ascending), (Type.author, Order.descending)]
        expected = [book3, book4, book1, book2]

        book_sorter = BookSorter()
        result = book_sorter.sort_books(bookshelf, rules)

        self.assertEqual(expected, result)

    def test_title_ordering_descending_author_ordering_ascending(self):
        rules = [(Type.title, Order.descending), (Type.author, Order.ascending)]
        expected = [book2, book1, book4, book3]

        book_sorter = BookSorter()
        result = book_sorter.sort_books(bookshelf, rules)

        self.assertEqual(expected, result)

    def test_title_ordering_descending_author_ordering_descending(self):
        rules = [(Type.title, Order.descending), (Type.author, Order.descending)]
        expected = [book2, book1, book4, book3]

        book_sorter = BookSorter()
        result = book_sorter.sort_books(bookshelf, rules)

        self.assertEqual(expected, result)

    def test_bookshelf_empty(self):
        rules = [(Type.title, Order.descending), (Type.author, Order.descending)]
        books = []
        expected = []

        book_sorter = BookSorter()
        result = book_sorter.sort_books(books, rules)
        self.assertEqual(expected, result)

    def test_rules_empty(self):
        rules = []
        expected = []

        book_sorter = BookSorter()
        result = book_sorter.sort_books(bookshelf, rules)
        self.assertEqual(expected, result)

    def test_rules_none(self):
        rules = None

        book_sorter = BookSorter()

        self.assertRaises(SortingServiceException, book_sorter.sort_books,
                          bookshelf, rules)

    def test_author_ordering_ascending_title_ordering_descending(self):
        rules = [(Type.author, Order.ascending), (Type.title, Order.descending)]
        expected = [book1, book4, book3, book2]

        book_sorter = BookSorter()
        result = book_sorter.sort_books(bookshelf, rules)

        self.assertEqual(expected, result)

    def test_edition_descending_author_descending_title_ascending(self):
        rules = [(Type.edition_year, Order.descending),
                 (Type.author, Order.descending), (Type.title, Order.ascending)]
        expected = [book4, book1, book3, book2]

        book_sorter = BookSorter()
        result = book_sorter.sort_books(bookshelf, rules)

        self.assertEqual(expected, result)

if __name__ == "__main__":
    tester.main()
