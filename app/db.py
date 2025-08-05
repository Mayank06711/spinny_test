from uuid import uuid4
from .schemas import  Seat
from .models import seats

def seed_seats(n: int = 10):
    if not seats:
        for i in range(1, n + 1):
            seat_id = str(uuid4())
            seats[seat_id] = Seat(id=seat_id, number=i)
    print("Seats are created successfully\n")