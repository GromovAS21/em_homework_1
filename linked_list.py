from typing import List


class DataDescriptor:
    """Дескриптор данных"""

    def __set_name__(self, owner, name):
        self.name = "__" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name, "Еще не установлено")

    def __set__(self, instance, value):
        setattr(instance, self.name, value)


class ObjList:
    """Класс элемента связанного списка"""

    prev = DataDescriptor()
    next = DataDescriptor()
    data = DataDescriptor()

    def __init__(self, data: str):
        self.prev = None
        self.next = None
        self.data = data

    def __str__(self):
        return self.data


class LinkedList:
    """Класс связанного списка"""
    obj_list = []

    def __init__(self):
        self.head = self.obj_list[0] if self.obj_list else None
        self.tail = self.obj_list[-1] if self.obj_list else None

    def add(self, obj: ObjList) -> None:
        """Добавляет элемент в конец связанного списка."""
        # Устанавливаем голову списка, если он пуст
        if not self.obj_list:
            self.head = obj
        # Устанавливаем ссылку на следующий элемент для предыдущего объекта
        if self.tail:
            self.tail.next = obj
        # Устанавливаем ссылку на предыдущий элемент для нового объекта
        obj.prev = self.tail
        # Обновляем хвост списка
        self.tail = obj
        self.obj_list.append(obj)

    def remove_obj(self) -> None:
        """Удаляет последний элемент из связного списка"""
        if self.obj_list:
            self.obj_list.pop()
            # Обновляем хвост списка
            self.tail = self.obj_list[-1] if self.obj_list else None
            # Убираем ссылку на следующий элемент у нового хвоста
            self.tail.next = None

    def get_data(self) -> List[str]:
        """Получение списка из строк данных во всех объeктах связного списка"""
        if self.obj_list:
            return [obj.data for obj in self.obj_list]
