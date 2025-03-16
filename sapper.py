import random


class Cell:
    """Класс ячейки игрового поля"""

    def __init__(self, around_mines: int = 0, mine: bool = False):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_mine = False

    def __str__(self):
        if self.mine and self.fl_mine:
            return "O"
        elif self.mine:
            return "*"
        elif self.fl_mine:
            return " "
        return "#"


class GamePole:
    """Класс игрового поля"""

    def __init__(self, field_area: int, count_mines: int):
        self.field_area = field_area
        self.count_mines = count_mines
        self.pole = self.init()

    def init(self) -> list:
        """Метод создания игрового поля"""
        count_cells = self.field_area * self.field_area
        cells = [Cell() for _ in range(count_cells)]
        cell_mines = random.sample(range(count_cells), self.count_mines)
        for cell_index in cell_mines:
            cells[cell_index].mine = True
        self.calculate_around_mines(cells)
        return cells

    def calculate_around_mines(self, cells: list) -> None:
        """Метод для подсчета мин вокруг каждой ячейки"""
        for i in range(self.field_area):
            for j in range(self.field_area):
                if not cells[i * self.field_area + j].mine:
                    count = 0
                    for x in range(i - 1, i + 2):
                        for y in range(j - 1, j + 2):
                            if 0 <= x < self.field_area and 0 <= y < self.field_area:
                                if cells[x * self.field_area + y].mine:
                                    count += 1
                    cells[i * self.field_area + j].around_mines = count

    def __show(self) -> None:
        """Метод отображения игрового поля"""
        for i in range(self.field_area):
            row = self.pole[i * self.field_area:(i + 1) * self.field_area]
            print("  ".join(map(str, row)))

    def open_cell(self, row: int, cell: int) -> None:
        """Метод открытия ячейки"""
        try:
            # Нахождение ячейки по координатам
            cell = self.pole[row * self.field_area - (self.field_area - cell) - 1]
            cell.fl_mine = True
            if cell.mine:
                print("Вы проиграли!")
        except IndexError:
            print("Такой ячейки нет!")
        finally:
            self.__show()
