from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    name: str
    is_active: bool = False

class UserUpdate(BaseModel):
    name: Optional[str] = None
    is_active: Optional[bool] = None

class User(BaseModel):
    id: str
    name: str

class Seat(BaseModel):
    id: str
    number: int
    is_booked: bool = False

class ChooseSeatRequest(BaseModel):
    user_id: str
    seat_number: int

class Ticket(BaseModel):
    id: str
    user_id: str
    seat_id: str

class BookTicketRequest(BaseModel):
    user_id: str
    seat_id: str