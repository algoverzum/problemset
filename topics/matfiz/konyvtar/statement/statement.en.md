## Library Catalog Sorting

There are $N$ books in a library; the title and publication year are known for each. The librarian wants to arrange the books on the shelf such that:
1. they are in ascending order by publication year,
2. if the year is the same, then in alphabetical order by title.

### Input
The first line contains an integer, $N$ &ndash; the number of books.

Then $N$ lines follow, each containing the data of a book: the book's title and its publication year. The book title is text without spaces, and the publication year is an integer.

### Constraints
- $1 \le N \le 1000$
- $1000 \le year \le 2024$

### Output
The books sorted in the specified order.

### Example Input

    5
    Algoritmusok 2010
    Adatszerkezetek 2010
    Python_kezdoknek 2018
    Mesterseges_intelligencia 2020
    Programozas_alapjai 2010

### Example Output

    Adatszerkezetek 2010
    Algoritmusok 2010
    Programozas_alapjai 2010
    Python_kezdoknek 2018
    Mesterseges_intelligencia 2020
