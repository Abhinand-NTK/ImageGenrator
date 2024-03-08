from pydantic import BaseModel

class UserBase(BaseModel):
    email: str
    user_type: str

class UserCreate(UserBase):
    password: str

class UserLogin(BaseModel):
    email: str
    password: str

class GenerateImageRequest(BaseModel):
    prompt: str
