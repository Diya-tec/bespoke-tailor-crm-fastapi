from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from database import engine, Base, get_db
from models import User
from schemas import UserCreate, UserResponse

app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#create table
Base.metadata.create_all(bind=engine)

#create users
@app.post("/users",response_model=UserResponse)
def create_user(user:UserCreate,db:Session=Depends(get_db)):
    new_user=User(
        name=user.name,
        phno=user.phno,
        shirt_shoulder=user.shirt_shoulder,
        shirt_length=user.shirt_length,
        shirt_hand=user.shirt_hand,
        pants_length=user.pants_length,
        pants_style=user.pants_style,
        pants_waist=user.pants_waist
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@app.get("/users",response_model=list[UserCreate])
def get_user(db:Session=Depends(get_db)):
    return db.query(User).all()

#read one user
@app.get("/users/{user_id}",response_model=UserResponse)
def get_user(user_id:int,db:Session=Depends(get_db)):
    user=db.query(User).filter(
        User.id==user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.put("/users/{user_id}",response_model=UserResponse)
def update(user_id:int, user_data:UserCreate, db:Session=Depends(get_db)):
    user=db.query(User).filter(
        User.id==user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user.name=user_data.name
    user.phno=user_data.phno
    user.shirt_shoulder=user_data.shirt_shoulder
    user.shirt_length=user_data.shirt_length
    user.shirt_hand=user_data.shirt_hand
    user.pants_length=user_data.pants_length
    user.pants_style=user_data.pants_style
    user.pants_waist=user_data.pants_waist

    db.commit()
    db.refresh(user)
    return user

@app.delete("/users/{user_id}")
def delete(user_id:int,db:Session=Depends(get_db)):
    user=db.query(User).filter(
        User.id==user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
      
    db.delete(user)
    db.commit()
    return {"message":"User deleted successfully"}