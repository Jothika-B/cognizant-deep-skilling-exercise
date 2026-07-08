from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from database import SessionLocal
from models import User

SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/register")
def register(username: str, password: str, db: Session = Depends(get_db)):
    hashed_password = pwd_context.hash(password)

    user = User(
        username=username,
        password=hashed_password
    )

    db.add(user)
    db.commit()

    return {"message": "User registered successfully"}


@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(),
          db: Session = Depends(get_db)):

    user = db.query(User).filter(
        User.username == form_data.username
    ).first()

    if not user:
        raise HTTPException(status_code=401, detail="Invalid username")

    if not pwd_context.verify(form_data.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid password")

    token = jwt.encode(
        {"sub": user.username},
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }


def get_current_user(token: str = Depends(oauth2_scheme)):

    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        username = payload.get("sub")

        if username is None:
            raise HTTPException(status_code=401)

        return username

    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid Token")


@router.get("/protected")
def protected_route(current_user: str = Depends(get_current_user)):
    return {
        "message": f"Welcome {current_user}! This is a protected route."
    }


@router.post("/logout")
def logout():
    return {
        "message": "Logout successful. Delete the token on the client side."
    }
