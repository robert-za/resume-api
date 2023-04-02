from sqlalchemy import Boolean, Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class WorkExperienceDB(Base):
    __tablename__ = 'work_experiences'

    id = Column(Integer, primary_key=True, index=True)
    company = Column(String, nullable=False)
    date_started = Column(String, nullable=False)
    date_ended = Column(String, nullable=True)
    position = Column(String, nullable=False)
    description = Column(String(256))
    person_id = Column(Integer, ForeignKey('persons.id'))
    person = relationship('PersonDB', back_populates='work_experience')
    skills = Column(String)
    

class EducationDB(Base):
    __tablename__ = 'educations'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    faculty = Column(String, nullable=False)
    degree = Column(String, nullable=False)
    date_started = Column(String, nullable=False)
    date_ended = Column(String, nullable=True)
    graduated = Column(Boolean, nullable=False)
    person_id = Column(Integer, ForeignKey('persons.id'))
    person = relationship('PersonDB', back_populates='education')
    

class AchievementDB(Base):
    __tablename__ = 'achievements'

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    person_id = Column(Integer, ForeignKey('persons.id'))
    person = relationship('PersonDB', back_populates='achievements')


class FreetimeDB(Base):
    __tablename__ = 'freetime'

    id = Column(Integer, primary_key=True, index=True)
    freetime_activity = Column(String, nullable=False)
    person_id = Column(Integer, ForeignKey('persons.id'))
    person = relationship('PersonDB', back_populates='freetime')


class PersonDB(Base):
    __tablename__ = 'persons'
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    birthdate = Column(Date, nullable=True)
    contact = relationship('ContactDB', uselist=False, back_populates='person')
    language = relationship('LanguageDB', uselist=True, back_populates='person')
    work_experience = relationship('WorkExperienceDB', back_populates='person')
    education = relationship('EducationDB', uselist=True, back_populates='person')
    achievements = relationship('AchievementDB', back_populates='person')
    freetime = relationship('FreetimeDB', back_populates='person')


class ContactDB(Base):
    __tablename__ = "contacts"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String)
    mobile = Column(String)
    person_id = Column(Integer, ForeignKey("persons.id"))
    person = relationship("PersonDB", back_populates="contact")


class LanguageDB(Base):
    __tablename__ = 'languages'
    id = Column(Integer, primary_key=True, index=True)
    language = Column(String)
    level = Column(String)
    person_id = Column(Integer, ForeignKey('persons.id'))
    person = relationship('PersonDB', back_populates='language')
