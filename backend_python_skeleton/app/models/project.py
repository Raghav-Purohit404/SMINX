from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.core.database import Base

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)
    skills_required = Column(String, nullable=True)  # Comma-separated list or handled as JSON elsewhere
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    # Relationship to the User model
    owner = relationship("User", back_populates="projects")

    # Optional timestamps
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f"<Project(id={self.id}, title='{self.title}', owner_id={self.owner_id})>"
