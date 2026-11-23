from pyramid.view import view_config


@view_config(route_name="home", renderer="json")
def home(request):
    return {
        "message": "REST API Manajemen Mahasiswa dan Matakuliah",
        "endpoints": ["/api/mahasiswa", "/api/matakuliah"],
    }
