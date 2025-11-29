from sqlalchemy import Column, String, Boolean, DateTime, JSON
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.database import Base  # updated import to match previous database.py

class User(Base):
    __tablename__ = "users"

    # -------- Primary Fields --------
    id = Column(String, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    email = Column(String(120), unique=True, nullable=False, index=True)

    # -------- Authentication --------
    hashed_password = Column(String, nullable=False)  # renamed for consistency
    email_verified = Column(Boolean, default=False)

    # -------- Skills --------
    # stored as JSON list: ["python", "react", "nodejs"]
    skills = Column(JSON, default=list)

    # -------- OTP for Email Verification --------
    otp_code = Column(String, nullable=True)
    otp_expiry = Column(DateTime(timezone=True), nullable=True)

    # -------- Timestamps --------
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # -------- Relationships (future expansion, optional) --------
    # projects = relationship("Project", back_populates="owner")
    # messages = relationship("Message", back_populates="sender")

    def __repr__(self):
        return f"<User {self.email}>"
