from sqlalchemy.orm import Session
from utils.jwt_handler import create_access_token
from models.user_model import User
from utils.hash import hash_password , verify_password
from fastapi import HTTPException
from utils.otphandler import generate_otp, save_otp, verify_otp, delete_otp
from utils.emailservice import send_otp_email



def register_user(db: Session, user):

    hashed_password = hash_password(user.password)

    new_user = User(
        username=user.username,
        email=user.email,
        password=hashed_password,
        role_id=3
    )
        # check if username already exists
    existing_user = db.query(User).filter(
        User.username == user.username
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Username already exists"
        )
    existing_email = db.query(User).filter(
        User.email == user.email
    ).first()

    if existing_email:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )
    db.add(new_user)

    db.commit()

    db.refresh(new_user)


    return new_user



def login_user(db: Session, user):
    db_user = db.query(User).filter(
    User.email == user.email
    ).first()

    if not db_user:
        return None

    if not verify_password(user.password, db_user.password):
        return None

    token = create_access_token({
        "username": db_user.username,
        "role": db_user.role
    })


    return {
        "access_token": token,
        "role": db_user.role
    }




def send_otp(db, email):

    user = db.query(User).filter(User.email == email).first()

    # if not user:
    #     raise HTTPException(status_code=404, detail="Email not registered")

    otp = generate_otp()

    save_otp(email, otp)

    send_otp_email(email, otp)

    return {"message": "OTP sent successfully"}


def verify_user_otp(email, otp):

    if not verify_otp(email, otp):
        raise HTTPException(status_code=400, detail="Invalid OTP")

    return {"message": "OTP verified"}


def reset_password(db, email, new_password):

    user = db.query(User).filter(User.email == email).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user.password = hash_password(new_password)

    db.commit()

    delete_otp(email)

    return {"message": "Password updated successfully"}