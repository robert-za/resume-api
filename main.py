from datetime import datetime
from fastapi import Depends, FastAPI, status
from sqlalchemy.orm import Session

import models
import schemas
from database import Base, SessionLocal, engine

Base.metadata.create_all(engine)
app = FastAPI()

def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


@app.get("/persons")
def get_persons(session: Session = Depends(get_session)):
    obj = session.query(models.Person).all()
    return obj

@app.post("/persons", response_model=schemas.Person, status_code=status.HTTP_201_CREATED)
def add_person(person: schemas.PersonCreate, session: Session = Depends(get_session)):
    obj = models.Person(
        first_name=person.first_name,
        last_name=person.last_name,
        birthdate=person.birthdate,
        contact=models.Contact(email=person.contact.email, mobile=person.contact.mobile),
        language=[models.Language(language=language.language, level=language.level) for language in person.language],
        work_experience=[models.WorkExperience(
            company=work_experience.company,
            # date_started=work_experience.date_started,
            # date_ended=work_experience.date_ended,
            position=work_experience.position,
            # skills=work_experience.skills,
            description=work_experience.description
        ) for work_experience in person.work_experience],
        education=[models.Education(
            name=education.name,
            faculty=education.faculty,
            degree=education.degree,
            # date_started=education.date_started,
            # date_ended=education.date_ended,
            graduated=education.graduated
        ) for education in person.education],
        achievements=[models.Achievements(
            description=achievement.description,
            year=achievement.year
        ) for achievement in person.achievements],
        freetime=[models.Freetime(freetime_activity=freetime.freetime_activity) for freetime in person.freetime]
    )
    session.add(obj)
    session.commit()
    session.refresh(obj)
    return obj
