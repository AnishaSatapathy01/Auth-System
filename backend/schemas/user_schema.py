from pydantic import BaseModel, EmailStr, Field


class UserCreate(BaseModel):

    username: str
    email: EmailStr
    password: str=Field(min_length=8, )
    

class UserLogin(BaseModel):

    email: EmailStr
    password: str
    
class EmailSchema(BaseModel):
    email: str

class OTPVerifySchema(BaseModel):
    email: str
    otp: str

class ResetPasswordSchema(BaseModel):
    email: str
    new_password: str

class AssignRoleSchema(BaseModel):
    email:str
    role:str