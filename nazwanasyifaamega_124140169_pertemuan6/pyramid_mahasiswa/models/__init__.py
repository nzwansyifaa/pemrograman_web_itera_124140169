from sqlalchemy import engine_from_config
from sqlalchemy.orm import configure_mappers, sessionmaker
import zope.sqlalchemy

from pyramid_mahasiswa.models.mahasiswa import Mahasiswa
from pyramid_mahasiswa.models.matakuliah import Matakuliah
from pyramid_mahasiswa.models.meta import Base

# Import semua model di atas agar terdaftar pada metadata Alembic.
configure_mappers()


def get_engine(settings, prefix="sqlalchemy."):
    return engine_from_config(settings, prefix)


def get_session_factory(engine):
    factory = sessionmaker()
    factory.configure(bind=engine)
    return factory


def get_tm_session(session_factory, transaction_manager):
    dbsession = session_factory()
    zope.sqlalchemy.register(dbsession, transaction_manager=transaction_manager)
    return dbsession


def includeme(config):
    settings = config.get_settings()
    settings["tm.manager_hook"] = "pyramid_tm.explicit_manager"
    engine = get_engine(settings)
    session_factory = get_session_factory(engine)
    config.registry["dbsession_factory"] = session_factory
    config.add_request_method(
        lambda request: get_tm_session(session_factory, request.tm),
        "dbsession",
        reify=True,
    )
