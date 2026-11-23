import pytest
from webtest import TestApp

from pyramid_mahasiswa import main
from pyramid_mahasiswa.models import Base, Mahasiswa, Matakuliah
from pyramid_mahasiswa.scripts.initialize_db import setup_models


@pytest.fixture
def api(tmp_path):
    database_path = (tmp_path / "api.sqlite").as_posix()
    app = main({}, **{"sqlalchemy.url": f"sqlite:///{database_path}"})
    engine = app.registry["dbsession_factory"].kw["bind"]
    Base.metadata.create_all(engine)
    try:
        yield TestApp(app)
    finally:
        Base.metadata.drop_all(engine)
        engine.dispose()


def test_matakuliah_crud_and_validation(api):
    assert api.get("/api/matakuliah").json == {"matakuliahs": []}

    created = api.post_json(
        "/api/matakuliah",
        {
            "kode_mk": "IF9999",
            "nama_mk": "Matakuliah Uji",
            "sks": 3,
            "semester": 5,
        },
    )
    assert created.status_code == 200
    item_id = created.json["matakuliah"]["id"]

    detail = api.get(f"/api/matakuliah/{item_id}")
    assert detail.json["matakuliah"]["kode_mk"] == "IF9999"

    updated = api.put_json(
        f"/api/matakuliah/{item_id}", {"sks": 4, "semester": 6}
    )
    assert updated.json["matakuliah"]["sks"] == 4
    assert updated.json["matakuliah"]["semester"] == 6

    invalid = api.post_json(
        "/api/matakuliah",
        {
            "kode_mk": "IF0000",
            "nama_mk": "Invalid",
            "sks": 0,
            "semester": 2,
        },
        status=400,
    )
    assert "bilangan bulat positif" in invalid.json["error"]

    duplicate = api.post_json(
        "/api/matakuliah",
        {
            "kode_mk": "IF9999",
            "nama_mk": "Duplikat",
            "sks": 3,
            "semester": 5,
        },
        status=400,
    )
    assert "sudah digunakan" in duplicate.json["error"]

    deleted = api.delete(f"/api/matakuliah/{item_id}")
    assert deleted.json["success"] is True
    api.get(f"/api/matakuliah/{item_id}", status=404)


def test_mahasiswa_crud_and_validation(api):
    assert api.get("/api/mahasiswa").json == {"mahasiswas": []}

    incomplete = api.post_json(
        "/api/mahasiswa",
        {"nama": "Tidak lengkap", "jurusan": "Informatika"},
        status=400,
    )
    assert "nim" in incomplete.json["error"]

    created = api.post_json(
        "/api/mahasiswa",
        {
            "nim": "TEST9999",
            "nama": "Mahasiswa Uji",
            "jurusan": "Teknik Informatika",
            "tanggal_lahir": "2002-01-15",
            "alamat": "Bandar Lampung",
        },
    )
    item_id = created.json["mahasiswa"]["id"]
    detail = api.get(f"/api/mahasiswa/{item_id}")
    assert detail.json["mahasiswa"]["nim"] == "TEST9999"

    updated = api.put_json(
        f"/api/mahasiswa/{item_id}", {"jurusan": "Sistem Informasi"}
    )
    assert updated.json["mahasiswa"]["jurusan"] == "Sistem Informasi"

    deleted = api.delete(f"/api/mahasiswa/{item_id}")
    assert deleted.json["success"] is True
    api.get(f"/api/mahasiswa/{item_id}", status=404)


def test_seed_data_is_idempotent(api):
    session_factory = api.app.registry["dbsession_factory"]
    dbsession = session_factory()
    try:
        setup_models(dbsession)
        dbsession.commit()
        setup_models(dbsession)
        dbsession.commit()
        assert dbsession.query(Mahasiswa).count() == 2
        assert dbsession.query(Matakuliah).count() == 3
    finally:
        dbsession.close()
