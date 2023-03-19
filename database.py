from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///todo.db')

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)


class ContactOrm(Base):
    __tablename__ = "contacts"
    id = Column(Integer, primary_key=True)
    email = Column(String(256))
    mobile = Column(String(32))
    
# class WorkExperienceOrm(Base):
#     company: str = Field(..., example="Webellian")
#     date_started: datetime = Field(..., example="2022-03-07T08:00")
#     date_ended: Union[datetime, str] = Field(None, example="Current Position")
#     position: str = Field(..., example="Junior Python Developer")
#     description: str


# class EducationOrm(Base):
#     name: str = Field(..., example="Arts et Métiers ParisTech")
#     faculty: str = Field(..., example="Mechanical Engineering and Applied Computer Science")
#     degree: str = Field(..., example="Master of Science")
#     date_started: datetime = Field(..., example="2011-09-01T08:00")
#     date_ended: datetime = Field(..., example="2015-02-01T08:00")
#     graduated: bool = Field(True, example=True)


# class AchievmentsOrm(Base):
#     description: str = Field(..., example="French Government Scholar")
#     date: int = Field(..., example=2014)


# class LanguageOrm(Base):
#     language: str = Field(..., example="English")
#     level: str = Field(..., example="C1")


# class FreetimeOrm(Base):
#     freetime_activity: str = Field(..., example="Travelling")
    

# class PersonOrm(Base):
#     first_name: str = Field(..., example="Robert")
#     last_name: str = Field(..., example="Zaniewski")
#     birthdate: Optional[datetime] = Field(None, example="1990-09-04T04:17")
#     contact: Contact
#     language: Language
#     work_experience: WorkExperience
#     education: Education
#     achievments: Achievments
#     freetime: Freetime