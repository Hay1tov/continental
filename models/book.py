from .user import User
from .room import Room

class Book:
    def __init__(self, type: str, room: int, price: str):
        self.type = type
        self.room = room
        self.price = price