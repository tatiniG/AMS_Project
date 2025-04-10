import psycopg2
from models.hospital import Hospital
from models.location import Location

class Controller:
    def __init__(self, view):
        self.view = view
        self.conn = psycopg2.connect(
            dbname="testdb", user="postgres", password="postgres", host="localhost", port="5432"
        )
        self.cursor = self.conn.cursor()
        self._initialize_database()

    def _initialize_database(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS location (
                id SERIAL PRIMARY KEY,
                city TEXT NOT NULL,
                state TEXT NOT NULL
            );
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS hospital (
                id SERIAL PRIMARY KEY,
                name TEXT NOT NULL,
                location_id INTEGER REFERENCES location(id)
            );
        """)
        self.conn.commit()

    def create_hospital(self, name, city, state):
        self.cursor.execute(
            "INSERT INTO location (city, state) VALUES (%s, %s) RETURNING id",
            (city, state)
        )
        location_id = self.cursor.fetchone()[0]

        self.cursor.execute(
            "INSERT INTO hospital (name, location_id) VALUES (%s, %s) RETURNING id",
            (name, location_id)
        )
        hospital_id = self.cursor.fetchone()[0]
        self.conn.commit()

        location = Location(city, state)
        hospital = Hospital(name, location)
        self.view.display_hospital(hospital)
