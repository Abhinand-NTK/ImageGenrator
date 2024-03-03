# # from fastapi import FastAPI, Depends, HTTPException, Response
# # import schemas
# # import database
# # from sqlalchemy.orm import Session
# # from models import User
# # from passlib.context import CryptContext
# # from fastapi.middleware.cors import CORSMiddleware
# # from dotenv import load_dotenv
# # import os


# # load_dotenv()


# # postgres_user = os.getenv("POSTGRES_USER")
# # postgres_password = os.getenv("POSTGRES_PASSWORD")
# # postgres_db = os.getenv("POSTGRES_DB")


# # app = FastAPI()

# # app.add_middleware(
# #     CORSMiddleware,
# #     allow_origins=["*"],
# #     allow_methods=["GET", "POST", "PUT", "DELETE"],
# #     allow_headers=["*"],
# # )

# # pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# # def get_db():
# #     db = database.SessionLocal()
# #     try:
# #         yield db
# #     finally:
# #         db.close()


# # @app.post("/signup/")
# # def signup(user: schemas.UserCreate, db: Session = Depends(get_db)):
# #     existing_user = db.query(User).filter(User.email == user.email).first()
# #     if existing_user:

# #         return Response(content="The user is alredy exist", status_code=400)

# #     # Create new user if email is not already in use
# #     hashed_password = pwd_context.hash(user.password)
# #     db_user = User(email=user.email, password=hashed_password,
# #                    user_type=user.user_type)
# #     db.add(db_user)
# #     db.commit()

# #     message = "User created successfully"
# #     return Response(content=message, status_code=200)


# # @app.post("/login/")
# # def login(user: schemas.UserLogin, db: Session = Depends(get_db)):
# #     db_user = db.query(User).filter(User.email == user.email).first()
# #     if not db_user or not pwd_context.verify(user.password, db_user.password):
# #         raise HTTPException(status_code=401, detail="Invalid credentials")
# #     return {"message": "Login successful"}


# # if __name__ == "__main__":
# #     import uvicorn
# #     uvicorn.run(app, host="127.0.0.1", port=8000)


# from fastapi import FastAPI, Depends, HTTPException, Response,Request
# from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
# from sqlalchemy.orm import Session
# from passlib.context import CryptContext
# from fastapi.middleware.cors import CORSMiddleware
# from dotenv import load_dotenv
# from jose import JWTError, jwt
# import os
# from datetime import datetime, timedelta
# import database
# import schemas
# from models import User
# from hashing import Hasher

# load_dotenv()

# # Load environment variables
# postgres_user = os.getenv("POSTGRES_USER")
# postgres_password = os.getenv("POSTGRES_PASSWORD")
# postgres_db = os.getenv("POSTGRES_DB")
# SECRET_KEY = os.getenv("SECRET_KEY")
# ALGORITHM = os.getenv("ALGORITHM")
# import os

# ACCESS_TOKEN_EXPIRE_MINUTES = int(os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))

# # ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

# # Create FastAPI app
# app = FastAPI()

# # Add CORS middleware
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_methods=["GET", "POST", "PUT", "DELETE"],
#     allow_headers=["*"],
# )

# # Initialize password hashing context
# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# # Define OAuth2 password bearer for token authentication
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# # Function to get database session
# def get_db():
#     db = database.SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# # Function to create access token
# def create_access_token(data: dict, expires_delta: timedelta):
#     to_encode = data.copy()
#     expire = datetime.utcnow() + expires_delta
#     to_encode.update({"exp": expire})
#     encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
#     return encoded_jwt

# # Function to verify token
# def verify_token(token: str, credentials_exception: HTTPException):
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         email: str = payload.get("sub")
#         if email is None:
#             raise credentials_exception
#         return email
#     except JWTError:
#         raise credentials_exception

# # Function to authenticate user
# def authenticate_user(db: Session, email: str, password: str):
#     user = db.query(User).filter(User.email == email).first()
#     if not user or not pwd_context.verify(password, user.password):
#         return False
#     return user

# @app.post("/token")
# async def login_for_access_token(request: Request, db: Session = Depends(get_db)):
#     data = await request.json()  # Extract data from request body
#     username = data.get("username")
#     password = data.get("password")

#     user = db.query(User).filter(User.email == username).first()
#     if not user or not Hasher.verify_password(password, user.password):
#         raise HTTPException(
#             status_code=401,
#             detail="Incorrect username or password",
#             headers={"WWW-Authenticate": "Bearer"},
#         )

#     # Generate and return access token if user is authenticated
#     access_token = create_access_token(data={"sub": user.username})
#     return {"access_token": access_token, "token_type": "bearer"}


# @app.post("/signup/")
# def signup(user: schemas.UserCreate, db: Session = Depends(get_db)):
#     existing_user = db.query(User).filter(User.email == user.email).first()
#     if existing_user:
#         return Response(content="The user already exists", status_code=400)
#     hashed_password = pwd_context.hash(user.password)
#     db_user = User(email=user.email, password=hashed_password, user_type=user.user_type)
#     db.add(db_user)
#     db.commit()
#     message = "User created successfully"
#     return Response(content=message, status_code=200)

# # Endpoint for user login
# @app.post("/login/")
# def login(user: schemas.UserLogin, db: Session = Depends(get_db)):
#     db_user = db.query(User).filter(User.email == user.email).first()
#     if not db_user or not pwd_context.verify(user.password, db_user.password):
#         raise HTTPException(status_code=401, detail="Invalid credentials")
#     return {"message": "Login successful"}

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="127.0.0.1", port=8000)


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

load_dotenv()

postgres_user = os.getenv("POSTGRES_USER")
postgres_password = os.getenv("POSTGRES_PASSWORD")
postgres_db = os.getenv("POSTGRES_DB")
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

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

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
