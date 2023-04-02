import os
from fastapi import Depends, FastAPI, status
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
import uvicorn

from . import models, schemas
from src.database import Base, SessionLocal, engine
from src.helpers import parse_pydantic_schema

Base.metadata.create_all(engine)
app = FastAPI()

def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

@app.post("/persons", status_code=status.HTTP_201_CREATED)
def add_person(person: schemas.PersonCreate, db: Session = Depends(get_session)):
    try:
        parsed_schema = parse_pydantic_schema(person)
        db_person = models.PersonDB(**parsed_schema)
        db.add(db_person)
        db.commit()
        db.refresh(db_person)
        return db_person
    except SQLAlchemyError as e:
        db.rollback()
        raise e

@app.get("/persons")
def get_persons(db: Session = Depends(get_session)):
    persons = db.query(models.PersonDB).all()
    return persons

@app.get("/contacts")
def get_contacts(db: Session = Depends(get_session)):
    contacts = db.query(models.ContactDB).all()
    return contacts

@app.get("/languages")
def get_languages(db: Session = Depends(get_session)):
    languages = db.query(models.LanguageDB).all()
    return languages

if __name__ == "__main__":
    port = os.getenv("PORT")
    if not port:
        port = 8080
    uvicorn.run(app, host="0.0.0.0", port=8080)
