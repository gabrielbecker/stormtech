from operator import itemgetter


class BookSorterAlgorithm:

    def sort(self, books, rules):
        """
        This method receives inputs already validated and will sort the books 
        set provided according with the rules provided.
        
        Arguments
             books (list): Books to be sorted
             rules (list of tuples): Rules (field and direction) to order the 
                                     books
            
        Returns:
            books (list): A list with the sorted books: 
        """

        """The first tuple has the highest priority, so first, we order with
        the rules with lower priority, leaving the highest one to the end
        where it will have a highest impact"""
        for type, order in reversed(rules):

            key = itemgetter(type.name)
            order = order.value

            books = sorted(books, key=key, reverse=order)

        return books
