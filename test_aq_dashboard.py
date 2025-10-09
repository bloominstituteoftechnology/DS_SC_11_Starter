import pytest
from aq_dashboard import app, DB, Record, get_results


@pytest.fixture
def client():
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test_db.sqlite3"
    client = app.test_client()

    with app.app_context():
        DB.create_all()

    yield client

    with app.app_context():
        DB.drop_all()


def test_root(client):
    with app.app_context():
        DB.session.add(Record(datetime="2023-10-18T00:00:00Z", value=22.5))
        DB.session.commit()

    response = client.get("/")
    assert response.status_code == 200
    assert b"Record" in response.data


def test_refresh(client):
    response = client.get("/refresh")
    assert response.status_code == 200
    assert b"Record" in response.data


def test_get_results():
    results = get_results()
    assert isinstance(results, list)
    assert all(isinstance(item, tuple) and len(item) == 2 for item in results)


def test_record_model():
    record = Record(id=1, datetime="2023-10-18T00:00:00Z", value=12.5)
    assert repr(record) == "Record: 1, 2023-10-18T00:00:00Z, 12.5"
