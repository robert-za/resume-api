from datetime import date, datetime
from typing import List, Optional

from pydantic import BaseModel, Field, validator

import models


class WorkExperience(BaseModel):
    company: str = Field(..., example="Webellion")
    date_started: datetime = Field(..., example=datetime(2000, 1, 1))
    date_ended: Optional[datetime] = Field(None, example=datetime(2000, 1, 1))
    position: str = Field(..., example="Junior Python Developer")
    skills: str = Field(..., example="Python|FastAPI|SQLAlchemy")
    description: str = Field(..., example="I was responsible for multiple projects.")
    class Meta:
        orm_model = models.WorkExperienceDB


class Education(BaseModel):
    name: str = Field(..., example="Arts et Métiers ParisTech")
    faculty: str = Field(..., example="Mechanical Engineering and Applied Computer Science")
    degree: str = Field(..., example="Master of Science")
    date_started: datetime = Field(..., example=datetime(2000, 1, 1))
    date_ended: Optional[datetime] = Field(None, example=datetime(2000, 1, 1))
    graduated: bool = Field(True, example=True)
    class Meta:
        orm_model = models.EducationDB


class Achievement(BaseModel):
    description: str = Field(..., example="French Government Scholar")
    year: int = Field(..., example=2014)
    class Meta:
        orm_model = models.AchievementDB


class Language(BaseModel):
    language: str = Field(..., example="English")
    level: str = Field(..., example="C1")
    class Meta:
        orm_model = models.LanguageDB


class Freetime(BaseModel):
    freetime_activity: str = Field(..., example="Travelling")
    class Meta:
        orm_model = models.FreetimeDB


class Contact(BaseModel):
    email: str = Field(..., example="johndoe@yahoo.com")
    mobile: str = Field(..., example="123456789")
    class Meta:
        orm_model = models.ContactDB


class PersonCreate(BaseModel):
    first_name: str = Field(..., example="Robert")
    last_name: str = Field(..., example="Z.")
    birthdate: Optional[date] = Field(None, example=date(2000, 1, 1))
    contact: Contact = Field(..., example=None)
    language: List[Language] = None
    work_experience: List[WorkExperience]
    education: List[Education]
    achievements: List[Achievement] = None
    freetime: List[Freetime] = None

    @validator("birthdate", pre=True)
    def parse_birthdate(cls, value):
        return datetime.strptime(
            value,
            "%Y-%m-%d"
        ).date()


class Person(PersonCreate):
    id: int = Field(..., example=1)
