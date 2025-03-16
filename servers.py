from typing import List


class Server:
    """Класс серверов"""
    id_server: int = 1

    def __init__(self):
        self.id: int = self.id_server
        self.connect: bool = False
        Server.id_server += 1

    def __str__(self):
        return f"№ {self.id}"


class Router:
    """Класс роутеров"""

    buffer: List["DataDescriptor"] = []
    instances_servers: List[int] = []

    def link(self, server: Server) -> None:
        """Соединение сервера с роутером"""
        if server.connect:
            print(f'Соединение сервера {server} с роутером уже установлено')
        else:
            server.connect = True
            self.instances_servers.append(server.id)  # добавляем в список активных серверов
            print(f'Соединение сервером {server} с роутером установлено')

    def unlink(self, server: Server) -> None:
        """Разрыв соединения сервера с роутером"""
        if server.connect:
            server.connect = False
            self.instances_servers.remove(server.id)  # удаляем из списка активных серверов
            print(f'Соединение сервера {server} с роутером разорвано')
        else:
            print(f'Соединение сервера {server} роутером отсутствует')

    def send_data(self) -> None:
        """Отправка данных серверу"""
        if not self.buffer:
            print("Данных для отправки нет")
        else:
            for data in self.buffer:
                if data.ip_address in self.instances_servers:
                    print(f"Данные серверу ID: {data.ip_address} отправлены")
                else:
                    print(f"Данные серверу ID: {data.ip_address} не отправлены")
            self.buffer.clear()


class Data:
    """Класс данных"""

    def __init__(self, data: str, ip_address: int):
        self.data: str = data
        self.ip_address: int = ip_address
        Router.buffer.append(self)
