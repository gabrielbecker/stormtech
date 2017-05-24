from enum import Enum


class Order(Enum):
    ascending = 0
    descending = 1


class Type(Enum):
    title = 0
    author = 1
    edition_year = 2
