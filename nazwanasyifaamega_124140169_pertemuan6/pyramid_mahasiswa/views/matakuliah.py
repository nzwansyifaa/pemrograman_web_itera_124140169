from pyramid.httpexceptions import HTTPBadRequest, HTTPNotFound
from pyramid.view import view_config

from pyramid_mahasiswa.models import Matakuliah


REQUIRED_FIELDS = ("kode_mk", "nama_mk", "sks", "semester")


def _json_object(request):
    try:
        data = request.json_body
    except (ValueError, TypeError) as error:
        raise HTTPBadRequest(
            json_body={"error": "Body harus berupa JSON yang valid."}
        ) from error
    if not isinstance(data, dict):
        raise HTTPBadRequest(json_body={"error": "Body JSON harus berupa object."})
    return data


def _positive_integer(value):
    return isinstance(value, int) and not isinstance(value, bool) and value > 0


def _validate(data, partial=False):
    fields = REQUIRED_FIELDS if not partial else tuple(
        field for field in REQUIRED_FIELDS if field in data
    )
    if not partial:
        missing = [field for field in REQUIRED_FIELDS if field not in data]
        if missing:
            return f"Field wajib belum diisi: {', '.join(missing)}."
    for field in fields:
        value = data.get(field)
        if field in ("kode_mk", "nama_mk"):
            if not isinstance(value, str) or not value.strip():
                return f"Field {field} wajib berupa teks dan tidak boleh kosong."
        elif not _positive_integer(value):
            return f"Field {field} harus berupa bilangan bulat positif."
    return None


def _duplicate_code(request, kode_mk, exclude_id=None):
    query = request.dbsession.query(Matakuliah).filter(
        Matakuliah.kode_mk == kode_mk
    )
    if exclude_id is not None:
        query = query.filter(Matakuliah.id != exclude_id)
    return query.first() is not None


@view_config(route_name="matakuliah_list", renderer="json")
def matakuliah_list(request):
    items = (
        request.dbsession.query(Matakuliah)
        .order_by(Matakuliah.id.asc())
        .all()
    )
    return {"matakuliahs": [item.to_dict() for item in items]}


@view_config(route_name="matakuliah_detail", renderer="json")
def matakuliah_detail(request):
    item = request.dbsession.get(Matakuliah, request.matchdict["id"])
    if item is None:
        return HTTPNotFound(json_body={"error": "Matakuliah tidak ditemukan."})
    return {"matakuliah": item.to_dict()}


@view_config(route_name="matakuliah_add", request_method="POST", renderer="json")
def matakuliah_add(request):
    data = _json_object(request)
    error = _validate(data)
    if error:
        return HTTPBadRequest(json_body={"error": error})
    data["kode_mk"] = data["kode_mk"].strip()
    data["nama_mk"] = data["nama_mk"].strip()
    if _duplicate_code(request, data["kode_mk"]):
        return HTTPBadRequest(json_body={"error": "kode_mk sudah digunakan."})

    item = Matakuliah(**{field: data[field] for field in REQUIRED_FIELDS})
    request.dbsession.add(item)
    request.dbsession.flush()
    return {"success": True, "matakuliah": item.to_dict()}


@view_config(route_name="matakuliah_update", request_method="PUT", renderer="json")
def matakuliah_update(request):
    item = request.dbsession.get(Matakuliah, request.matchdict["id"])
    if item is None:
        return HTTPNotFound(json_body={"error": "Matakuliah tidak ditemukan."})
    data = _json_object(request)
    if not data:
        return HTTPBadRequest(json_body={"error": "Body JSON tidak boleh kosong."})
    error = _validate(data, partial=True)
    if error:
        return HTTPBadRequest(json_body={"error": error})
    if "kode_mk" in data:
        data["kode_mk"] = data["kode_mk"].strip()
        if _duplicate_code(request, data["kode_mk"], item.id):
            return HTTPBadRequest(json_body={"error": "kode_mk sudah digunakan."})
    if "nama_mk" in data:
        data["nama_mk"] = data["nama_mk"].strip()
    for field in REQUIRED_FIELDS:
        if field in data:
            setattr(item, field, data[field])
    return {"success": True, "matakuliah": item.to_dict()}


@view_config(
    route_name="matakuliah_delete", request_method="DELETE", renderer="json"
)
def matakuliah_delete(request):
    item = request.dbsession.get(Matakuliah, request.matchdict["id"])
    if item is None:
        return HTTPNotFound(json_body={"error": "Matakuliah tidak ditemukan."})
    request.dbsession.delete(item)
    return {"success": True, "message": "Matakuliah berhasil dihapus."}
