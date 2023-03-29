from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel, Field

class AbstractBaseModel(BaseModel):
    class Config:
        orm_mode = True


class Contact(AbstractBaseModel):
    email: str = Field(..., example="rbt.zaniewski@gmail.com")
    mobile: str = Field(..., example="(+48) 607 459 434")


class WorkExperience(AbstractBaseModel):
    company: str = Field(..., example="Webellian")
    date_started: str = Field(..., example="2022-03-07T08:00")
    date_ended: Optional[str] = Field(None, example="2015-02-01T08:00")
    position: str = Field(..., example="Junior Python Developer")
    skill: List[str] = Field(..., example=["Python", "FastAPI", "SQLAlchemy"])
    description: str = Field(..., example="I was responsible for multiple projects.")


class Education(AbstractBaseModel):
    name: str = Field(..., example="Arts et Métiers ParisTech")
    faculty: str = Field(..., example="Mechanical Engineering and Applied Computer Science")
    degree: str = Field(..., example="Master of Science")
    date_started: str = Field(..., example="2011-09-01T08:00")
    date_ended: Optional[str] = Field(None, example="2015-02-01T08:00")
    graduated: bool = Field(True, example=True)


class Achievements(AbstractBaseModel):
    description: str = Field(..., example="French Government Scholar")
    year: int = Field(..., example=2014)


class Language(AbstractBaseModel):
    language: str = Field(..., example="English")
    level: str = Field(..., example="C1")


class Freetime(AbstractBaseModel):
    freetime_activity: str = Field(..., example="Travelling")

class PersonCreate(AbstractBaseModel):
    first_name: str = Field(..., example="Robert")
    last_name: str = Field(..., example="Zaniewski")
    birthdate: Optional[str] = Field(None, example="1990-09-04T04:17")
    contact: Contact
    language: List[Language]
    work_experience: List[WorkExperience]
    education: List[Education]
    achievements: List[Achievements]
    freetime: List[Freetime]

class Person(AbstractBaseModel):
    id: int = Field(..., example=1)
    first_name: str = Field(..., example="Robert")
    last_name: str = Field(..., example="Zaniewski")
    birthdate: Optional[str] = Field(None, example="1990-09-04T04:17")
    contact: Contact
    language: List[Language]
    work_experience: List[WorkExperience]
    education: List[Education]
    achievements: List[Achievements]
    freetime: List[Freetime]
