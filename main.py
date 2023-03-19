from fastapi import FastAPI, Depends
import schemas

from database import Base, engine, SessionLocal
from sqlalchemy.orm import Session

Base.metadata.create_all(engine)

def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

app = FastAPI()


@app.get("/")
def get_items(session: Session = Depends(get_session)):
    obj = session.query(schemas.ContactOrm).all()
    return obj

# @app.get("/{id}")
# def get_item(id: int, session: Session = Depends(get_session)):
#     obj = session.query(schemas.Item).get(id)
#     return obj

# @app.post("/")
# def add_item(item: schemas.Item, session: Session = Depends(get_session)):
#     obj = schemas.Item(task = item.task)
#     session.add(obj)
#     session.commit()
#     session.refresh(obj)
#     return obj

# @app.put("/{id}")
# def update_item(id: int, item: schemas.Item, session: Session = Depends(get_session)):
#     obj = session.query(schemas.Item).get(id)
#     obj.task = item.task
#     session.commit()
#     return obj

# @app.delete("/{id}")
# def delete_item(id: int, session: Session = Depends(get_session)):
#     obj = session.query(schemas.Item).get(id)
#     session.delete(obj)
#     session.commit()
#     session.close()
#     return f"Item id#{id} has been removed."