
from fastapi import FastAPI, Depends, HTTPException, Response, Request
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from jose import JWTError, jwt
import os
from datetime import datetime, timedelta
import database
import schemas
from models import User
from fastapi.responses import JSONResponse
from openai import OpenAI

load_dotenv()

postgres_user = os.getenv("POSTGRES_USER")
postgres_password = os.getenv("POSTGRES_PASSWORD")
postgres_db = os.getenv("POSTGRES_DB")
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
API_KEY = os.getenv("API_KEY")

ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_access_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(token: str, credentials_exception: HTTPException):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        return email
    except JWTError:
        raise credentials_exception

def authenticate_user(db: Session, email: str, password: str):
    user = db.query(User).filter(User.email == email).first()
    if not user or not pwd_context.verify(password, user.password):
        return False
    return user

@app.post("/token")
async def login_for_access_token(request: Request, db: Session = Depends(get_db)):
    data = await request.json()  
    username = data.get("username")
    password = data.get("password")

    user = db.query(User).filter(User.email == username).first()
    if not user or not pwd_context.verify(password, user.password):
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = create_access_token(data={"sub": user.email}, expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    return {"access_token": access_token, "token_type": "bearer"}


@app.post("/signup/")
def signup(user: schemas.UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        return Response(content="The user already exists", status_code=400)
    hashed_password = pwd_context.hash(user.password)
    db_user = User(email=user.email, password=hashed_password, user_type=user.user_type)
    db.add(db_user)
    db.commit()
    message = "User created successfully"
    return Response(content=message, status_code=200)

@app.post("/login/")
def login(user: schemas.UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if not db_user or not pwd_context.verify(user.password, db_user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"message": "Login successful"}


@app.post("/generate_image")
async def generate_image(request_data: schemas.GenerateImageRequest):
  
    try:
        client = OpenAI(api_key=API_KEY)
        print(API_KEY)
        print(request_data.prompt)

        response = client.images.generate(
            model="dall-e-2",
            prompt=request_data.prompt,
            size="1024x1024",
            quality="standard",
            n=1,
        )
        print("response")
        print("res:-",response)

        # response = client.images.generate(
        #     model="dall-e-2",
        #     prompt=data,
        #     size="1024x1024",
        #     quality="standard",
        #     n=1,
        # )

        output = response.data[0].url
        print(response.data[0].url)
        print(output)
        return JSONResponse(content={"data": output}, status_code=200)
    except Exception as e:
        return HTTPException(status_code=500, detail=str(e))
    


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
