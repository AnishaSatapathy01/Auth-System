from jose import jwt
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError , jwt
from fastapi import Depends , HTTPException 
from app.database import get_db
from sqlalchemy.orm import Session
from models.user_model import User
SECRET_KEY = "supersecretkeyNyx001"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

def create_access_token(data: dict):

    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    to_encode.update({"exp": expire})

    token = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return token
def get_current_user(
        token: str = Depends(oauth2_scheme),
        db: Session = Depends(get_db)
):

    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials"
    )

    try:

        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        email: str = payload.get("sub")

        if email is None:
            raise credentials_exception

    except JWTError:

        raise credentials_exception


    user = db.query(User).filter(User.email == email).first()

    if user is None:
        raise credentials_exception

    return user