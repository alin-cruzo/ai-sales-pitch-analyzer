from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base

class Pitch(Base):
    __tablename__ = "pitches"

    id = Column(Integer, primary_key=True, index=True)
    transcript = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Link to the feedback
    feedback = relationship("Feedback", back_populates="pitch", uselist=False)

class Feedback(Base):
    __tablename__ = "feedback"

    id = Column(Integer, primary_key=True, index=True)
    pitch_id = Column(Integer, ForeignKey("pitches.id"))
    ai_critique = Column(Text, nullable=False)
    audio_file_path = Column(String, nullable=True) 
    created_at = Column(DateTime, default=datetime.utcnow)

    # Link back to the pitch
    pitch = relationship("Pitch", back_populates="feedback")