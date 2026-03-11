from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    username = Column(String(50), unique=True)

    email = Column(String(100), unique=True)

    password = Column(String(255))

    role_id = Column(Integer, ForeignKey("roles.id"))
    role = relationship("Role")

class Role(Base):

    __tablename__ = "roles"

    id = Column(Integer, primary_key=True)
    name = Column(String)