from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)

def test_add_person():
    new_person = {
        "first_name": "Robert",
        "last_name": "Zaniewski",
        "birthdate": "2000-01-01"
        }
    response = client.post("/persons", json=new_person)
    assert response.status_code == 201
    assert response.json()['birthdate'] == '2000-01-01'
    assert response.json()['first_name'] == 'Robert'
    assert response.json()['last_name'] == 'Z.'
    assert "id" in response.json()
