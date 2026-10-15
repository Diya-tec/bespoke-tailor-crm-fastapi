from pydantic import BaseModel

class UserCreate(BaseModel):
    name:str
    phno:int
    shirt_shoulder:int
    shirt_length:int
    shirt_hand:str
    pants_length:int
    pants_style:str
    pants_waist:int

class UserResponse(BaseModel):
    id:int
    name:str
    phno:int
    shirt_shoulder:int
    shirt_length:int
    shirt_hand:str
    pants_length:int
    pants_style:str
    pants_waist:int

    class Config:
        from_attributes=True