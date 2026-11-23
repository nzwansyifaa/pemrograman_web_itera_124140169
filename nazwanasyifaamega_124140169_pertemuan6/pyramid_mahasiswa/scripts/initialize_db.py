import argparse
import sys
from datetime import date

from pyramid.paster import bootstrap, setup_logging
from sqlalchemy.exc import OperationalError

from pyramid_mahasiswa.models import Mahasiswa, Matakuliah


SEED_MAHASISWA = (
    {
        "nim": "12345",
        "nama": "Budi Santoso",
        "jurusan": "Teknik Informatika",
        "tanggal_lahir": date(2000, 5, 15),
        "alamat": "Bandung",
    },
    {
        "nim": "54321",
        "nama": "Siti Aminah",
        "jurusan": "Sistem Informasi",
        "tanggal_lahir": date(2001, 8, 22),
        "alamat": "Jakarta",
    },
)

SEED_MATAKULIAH = (
    {"kode_mk": "IF2110", "nama_mk": "Pemrograman Web", "sks": 3, "semester": 3},
    {"kode_mk": "IF3140", "nama_mk": "Basis Data", "sks": 4, "semester": 5},
    {"kode_mk": "IF2120", "nama_mk": "Struktur Data", "sks": 3, "semester": 3},
)


def setup_models(dbsession):
    """Insert sample rows once; safe to run repeatedly."""
    for values in SEED_MAHASISWA:
        exists = dbsession.query(Mahasiswa.id).filter_by(nim=values["nim"]).first()
        if exists is None:
            dbsession.add(Mahasiswa(**values))

    for values in SEED_MATAKULIAH:
        exists = (
            dbsession.query(Matakuliah.id)
            .filter_by(kode_mk=values["kode_mk"])
            .first()
        )
        if exists is None:
            dbsession.add(Matakuliah(**values))


def parse_args(argv):
    parser = argparse.ArgumentParser(description="Seed data aplikasi Pyramid.")
    parser.add_argument("config_uri", help="File konfigurasi, contoh: development.ini")
    return parser.parse_args(argv[1:])


def main(argv=sys.argv):
    args = parse_args(argv)
    setup_logging(args.config_uri)
    env = bootstrap(args.config_uri)
    try:
        with env["request"].tm:
            setup_models(env["request"].dbsession)
        print("Data contoh mahasiswa dan matakuliah berhasil disiapkan.")
    except OperationalError as error:
        print(f"Tidak dapat terhubung ke database: {error}", file=sys.stderr)
        return 1
    finally:
        env["closer"]()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
