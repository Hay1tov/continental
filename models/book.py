from .user import User
from .room import Room

class Book:
<<<<<<< HEAD
    def __init__(self, type: str, room: int, price: str):
        self.type = type
        self.room = room
        self.price = price


=======
    def __init__(self, user: User, room: Room):
        self.user = user
        self.room = room
    
>>>>>>> 2bb8dd54d92e910f33c6e7321c72cf1ea5493f79
