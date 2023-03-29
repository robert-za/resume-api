from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel, Field


class Contact(BaseModel):
    email: str = Field(..., example="rbt.zaniewski@gmail.com")
    mobile: str = Field(..., example="(+48) 607 459 434")


class WorkExperience(BaseModel):
    company: str = Field(..., example="Webellian")
    # date_started: datetime = Field(..., example="2022-03-07T08:00")
    # date_ended: Optional[datetime] = Field(None, example="2015-02-01T08:00")
    position: str = Field(..., example="Junior Python Developer")
    # skills: List[str] = Field(..., example=["Python", "FastAPI", "SQLAlchemy"])
    description: str = Field(..., example="I was responsible for multiple projects.")


class Education(BaseModel):
    name: str = Field(..., example="Arts et Métiers ParisTech")
    faculty: str = Field(..., example="Mechanical Engineering and Applied Computer Science")
    degree: str = Field(..., example="Master of Science")
    # date_started: datetime = Field(..., example="2011-09-01T08:00")
    # date_ended: Optional[datetime] = Field(None, example="2015-02-01T08:00")
    graduated: bool = Field(True, example=True)


class Achievements(BaseModel):
    description: str = Field(..., example="French Government Scholar")
    year: int = Field(..., example=2014)


class Language(BaseModel):
    language: str = Field(..., example="English")
    level: str = Field(..., example="C1")


class Freetime(BaseModel):
    freetime_activity: str = Field(..., example="Travelling")

class PersonCreate(BaseModel):
    first_name: str = Field(..., example="Robert")
    last_name: str = Field(..., example="Zaniewski")
    birthdate: Optional[datetime] = Field(None, example="1990-09-04T04:17")
    contact: Contact
    language: List[Language]
    work_experience: List[WorkExperience]
    education: List[Education]
    achievements: List[Achievements]
    freetime: List[Freetime]

class Person(BaseModel):
    id: int = Field(..., example=1)
    first_name: str = Field(..., example="Robert")
    last_name: str = Field(..., example="Zaniewski")
    birthdate: Optional[datetime] = Field(None, example="1990-09-04T04:17")
    contact: Contact
    language: List[Language]
    work_experience: List[WorkExperience]
    education: List[Education]
    achievements: List[Achievements]
    freetime: List[Freetime]
    
    class Config:
        orm_mode = True