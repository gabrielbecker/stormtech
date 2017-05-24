from BookSorterAlgorithm import BookSorterAlgorithm


class BookSorter:

    def sort_books(self, books, rules):
        """
        This top level method will check inputs variables condition and order
        the provided books with the provided rules.
        
        Arguments:
            books (list): Books to be sorted
            rules (list of tuples): Rules (field and direction) to order the 
                                    books
        
        Returns:
            books (list): A list with the sorted books
            
        Exceptions:
            SortingServiceException: When the rules or books are null
        """

        if rules is None:
            raise SortingServiceException

        if books is None:
            raise SortingServiceException

        if not rules:
            books = []
            return books

        bs_algorithm = BookSorterAlgorithm()
        books = bs_algorithm.sort(books, rules)

        return books


class SortingServiceException(Exception):
    """Trigered when rules or books are null"""
