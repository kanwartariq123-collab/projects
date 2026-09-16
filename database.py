import psycopg2

DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "database": "studentdb",
    "user": "postgres",
    "password": "admin@40123"
}


def get_db():
    return psycopg2.connect(**DB_CONFIG)