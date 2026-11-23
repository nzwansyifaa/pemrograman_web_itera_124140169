from datetime import date

from pyramid.httpexceptions import HTTPBadRequest, HTTPNotFound
from pyramid.view import view_config

from pyramid_mahasiswa.models import Mahasiswa


_REQUIRED_FIELDS = ("nim", "nama", "jurusan")


def _body(request):
    try:
        data = request.json_body
    except (ValueError, TypeError) as error:
        raise HTTPBadRequest(
            json_body={"error": "Body harus berupa JSON yang valid."}
        ) from error
    if not isinstance(data, dict):
        raise HTTPBadRequest(json_body={"error": "Body JSON harus berupa object."})
    return data


def _validate(data, partial=False):
    if not partial:
        missing = [field for field in _REQUIRED_FIELDS if not data.get(field)]
        if missing:
            return f"Field wajib belum diisi: {', '.join(missing)}."
    for field in _REQUIRED_FIELDS:
        if field in data and (not isinstance(data[field], str) or not data[field].strip()):
            return f"Field {field} wajib berupa teks dan tidak boleh kosong."
    if "tanggal_lahir" in data and data["tanggal_lahir"]:
        try:
            date.fromisoformat(data["tanggal_lahir"])
        except (TypeError, ValueError):
            return "tanggal_lahir harus menggunakan format YYYY-MM-DD."
    return None


def _as_date(value):
    return date.fromisoformat(value) if value else None


@view_config(route_name="mahasiswa_list", renderer="json")
def mahasiswa_list(request):
    items = request.dbsession.query(Mahasiswa).order_by(Mahasiswa.id.asc()).all()
    return {"mahasiswas": [item.to_dict() for item in items]}


@view_config(route_name="mahasiswa_detail", renderer="json")
def mahasiswa_detail(request):
    item = request.dbsession.get(Mahasiswa, request.matchdict["id"])
    if item is None:
        return HTTPNotFound(json_body={"error": "Mahasiswa tidak ditemukan."})
    return {"mahasiswa": item.to_dict()}


@view_config(route_name="mahasiswa_add", request_method="POST", renderer="json")
def mahasiswa_add(request):
    data = _body(request)
    error = _validate(data)
    if error:
        return HTTPBadRequest(json_body={"error": error})
    nim = data["nim"].strip()
    if request.dbsession.query(Mahasiswa).filter_by(nim=nim).first():
        return HTTPBadRequest(json_body={"error": "nim sudah digunakan."})
    item = Mahasiswa(
        nim=nim,
        nama=data["nama"].strip(),
        jurusan=data["jurusan"].strip(),
        tanggal_lahir=_as_date(data.get("tanggal_lahir")),
        alamat=data.get("alamat"),
    )
    request.dbsession.add(item)
    request.dbsession.flush()
    return {"success": True, "mahasiswa": item.to_dict()}


@view_config(route_name="mahasiswa_update", request_method="PUT", renderer="json")
def mahasiswa_update(request):
    item = request.dbsession.get(Mahasiswa, request.matchdict["id"])
    if item is None:
        return HTTPNotFound(json_body={"error": "Mahasiswa tidak ditemukan."})
    data = _body(request)
    if not data:
        return HTTPBadRequest(json_body={"error": "Body JSON tidak boleh kosong."})
    error = _validate(data, partial=True)
    if error:
        return HTTPBadRequest(json_body={"error": error})
    if "nim" in data:
        nim = data["nim"].strip()
        duplicate = request.dbsession.query(Mahasiswa).filter(
            Mahasiswa.nim == nim, Mahasiswa.id != item.id
        ).first()
        if duplicate:
            return HTTPBadRequest(json_body={"error": "nim sudah digunakan."})
        item.nim = nim
    for field in ("nama", "jurusan", "alamat"):
        if field in data:
            value = data[field]
            setattr(item, field, value.strip() if isinstance(value, str) else value)
    if "tanggal_lahir" in data:
        item.tanggal_lahir = _as_date(data["tanggal_lahir"])
    return {"success": True, "mahasiswa": item.to_dict()}


@view_config(
    route_name="mahasiswa_delete", request_method="DELETE", renderer="json"
)
def mahasiswa_delete(request):
    item = request.dbsession.get(Mahasiswa, request.matchdict["id"])
    if item is None:
        return HTTPNotFound(json_body={"error": "Mahasiswa tidak ditemukan."})
    request.dbsession.delete(item)
    return {"success": True, "message": "Mahasiswa berhasil dihapus."}
