from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from schemas.user_schema import UserCreate, UserLogin, EmailSchema



from services import auth_service


router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)


@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):

    return auth_service.register_user(db, user)



@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):

    result = auth_service.login_user(db, user)

    if not result:
        return {"error": "Invalid username or password"}

    return result
@router.post("/send-otp")
def send_otp(data: EmailSchema, db: Session = Depends(get_db)):

    return auth_service.send_otp(db, data.email)