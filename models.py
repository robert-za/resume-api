from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime as dt
from database import Base


class Contact(Base):
    __tablename__ = 'contacts'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    mobile = Column(String, nullable=False)
    person_id = Column(Integer, ForeignKey('persons.id'))
    person = relationship('Person', back_populates='contact')


class WorkExperience(Base):
    __tablename__ = 'work_experiences'

    id = Column(Integer, primary_key=True, index=True)
    company = Column(String, nullable=False)
    # date_started = Column(DateTime(timezone=True), nullable=False)
    # date_ended = Column(DateTime(timezone=True), nullable=True)
    position = Column(String, nullable=False)
    # skills = Column(String, nullable=False)
    description = Column(String(256))
    person_id = Column(Integer, ForeignKey('persons.id'))
    person = relationship('Person', back_populates='work_experience')


class Education(Base):
    __tablename__ = 'educations'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    faculty = Column(String, nullable=False)
    degree = Column(String, nullable=False)
    # date_started = Column(DateTime(timezone=True), nullable=False)
    # date_ended = Column(DateTime(timezone=True), nullable=True)
    graduated = Column(Boolean, nullable=False)
    person_id = Column(Integer, ForeignKey('persons.id'))
    person = relationship('Person', back_populates='education')


class Achievements(Base):
    __tablename__ = 'achievements'

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    person_id = Column(Integer, ForeignKey('persons.id'))
    person = relationship('Person', back_populates='achievements')


class Language(Base):
    __tablename__ = 'languages'

    id = Column(Integer, primary_key=True, index=True)
    language = Column(String, nullable=False)
    level = Column(String, nullable=False)
    person_id = Column(Integer, ForeignKey('persons.id'))
    person = relationship('Person', back_populates='language')


class Freetime(Base):
    __tablename__ = 'freetime'

    id = Column(Integer, primary_key=True, index=True)
    freetime_activity = Column(String, nullable=False)
    person_id = Column(Integer, ForeignKey('persons.id'))
    person = relationship('Person', back_populates='freetime')


class Person(Base):
    __tablename__ = 'persons'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    birthdate = Column(DateTime(timezone=True), nullable=True)
    contact = relationship('Contact', uselist=False, back_populates='person')
    language = relationship('Language', back_populates='person')
    work_experience = relationship('WorkExperience', back_populates='person')
    education = relationship('Education', back_populates='person')
    achievements = relationship('Achievements', back_populates='person')
    freetime = relationship('Freetime', back_populates='person')