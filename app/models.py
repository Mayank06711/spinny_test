from typing import Dict
from .schemas import User, Seat, Ticket

# In-memory "databases"
users: Dict[str, User] = {}
seats: Dict[str, Seat] = {}
tickets: Dict[str, Ticket] = {}