from uuid import uuid4
from fastapi import HTTPException
from .models import users, seats, tickets
from .schemas import User, UserCreate, UserUpdate, Seat, ChooseSeatRequest, Ticket, BookTicketRequest

admin_key = "mayank"

def create_user(user: UserCreate) -> User:
    user_id = str(uuid4())
    new_user = User(id=user_id, name=user.name, is_active=True)#matlab signed up successfull
    users[user_id] = new_user   
    print(f"User {new_user.name} created successfully\n")
    return new_user

def update_user(user_id: str, user_update: UserUpdate) -> User:
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    user = users[user_id]
    if user_update.name is not None:
        user.name = user_update.name
    users[user_id] = user
    return user

def choose_seat(req: ChooseSeatRequest) -> Seat:
    seat = next((s for s in seats.values() if s.number == req.seat_number), None)
    if not seat:
        raise HTTPException(status_code=404, detail="Seat not found")
    if seat.is_booked:
        raise HTTPException(status_code=400, detail="Seat already booked")
    return seat

def book_ticket(req: BookTicketRequest) -> Ticket:
    if req.user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    if req.seat_id not in seats:
        raise HTTPException(status_code=404, detail="Seat not found")
    seat = seats[req.seat_id]
    if seat.is_booked:
        raise HTTPException(status_code=400, detail="Seat already booked")
    seat.is_booked = True
    ticket_id = str(uuid4())
    ticket = Ticket(id=ticket_id, user_id=req.user_id, seat_id=req.seat_id)
    tickets[ticket_id] = ticket
    return ticket