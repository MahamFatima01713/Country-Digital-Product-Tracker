from sqlalchemy import Column, Date, Integer, String, Text

from database import Base


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), nullable=False)
    country = Column(String(100), nullable=False)
    owner = Column(String(100), nullable=True)
    topic = Column(String(50), nullable=True)
    status = Column(String(50), nullable=False, default="Not Started")
    next_milestone = Column(String(300), nullable=True)
    milestone_date = Column(Date, nullable=True)
    status_note = Column(Text, nullable=True)
