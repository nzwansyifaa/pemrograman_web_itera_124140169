from pyramid.config import Configurator


def main(global_config, **settings):
    """WSGI application factory for Pyramid."""
    with Configurator(settings=settings) as config:
        config.include("pyramid_tm")
        config.include("pyramid_mahasiswa.models")
        config.include("pyramid_mahasiswa.routes")
        config.scan("pyramid_mahasiswa.views")
    return config.make_wsgi_app()
