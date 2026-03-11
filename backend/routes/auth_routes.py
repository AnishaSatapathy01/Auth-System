from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.user_model import User
from app.database import get_db
from schemas.user_schema import UserCreate, UserLogin, EmailSchema, OTPVerifySchema, ResetPasswordSchema, AssignRoleSchema
from utils.jwt_handler import get_current_user

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


@router.post("/verify-otp")
def verify_otp(data: OTPVerifySchema):

    return auth_service.verify_user_otp(data.email, data.otp)


@router.post("/reset-password")
def reset_password(data: ResetPasswordSchema, db: Session = Depends(get_db)):

    return auth_service.reset_password(db, data.email, data.new_password)

@router.post("/assign-role")
def assign_role(data: AssignRoleSchema, db: Session = Depends(get_db)):

    user = db.query(User).filter(User.email == data.email).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user.role = data.role

    db.commit()

    return {"message": "Role updated"}

@router.get("/users")
def get_users(db: Session = Depends(get_db)):

    users = db.query(users).all()

    return users