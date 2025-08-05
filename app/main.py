from fastapi import FastAPI
from . import db, controller, schemas

app = FastAPI()

# here we create seats before server can start.. so we mimic db
@app.on_event("startup")
def startup_event():
    db.seed_seats()

# create users
@app.post("/create_user", response_model=schemas.User)
def create_user(user: schemas.UserCreate):
    return controller.create_user(user)

@app.put("/update_user/{user_id}", response_model=schemas.User)
def update_user(user_id: str, user_update: schemas.UserUpdate):
    return controller.update_user(user_id, user_update)

@app.post("/choose_seat", response_model=schemas.Seat)
def choose_seat(req: schemas.ChooseSeatRequest):
    return controller.choose_seat(req)

@app.post("/book_ticket", response_model=schemas.Ticket)
def book_ticket(req: schemas.BookTicketRequest):
    return controller.book_ticket(req)