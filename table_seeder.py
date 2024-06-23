from Database.books import Books
from Table.row import Row
from Table.cell import Cell
from Table.table import Table

class TableSeeder:
    def __init__(self):
        pass

    @staticmethod
    def generate_table():
        books = Books.get_all()
        rows = []
        for book in books:
            cells = []
            for col in book:
                cells.append(Cell(100, col, 15))
            rows.append(Row(cells))

        return Table(rows)
