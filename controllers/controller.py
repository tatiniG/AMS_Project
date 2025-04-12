import psycopg2
from models.hospital import Hospital
from models.location import Location
from models.patient import Patient

class Controller:
    def __init__(self, view):
        self.view = view
        self.conn = psycopg2.connect(
            dbname="testdb", user="postgres", password="postgres", host="localhost", port="5432"
        )
        self.cursor = self.conn.cursor()

    def get_all_patients(self):
        self.cursor.execute("SELECT * FROM patient LIMIT 10;")
        rows = self.cursor.fetchall()
        return [Patient(*row) for row in rows]
    
    def get_all_locations(self):
        self.cursor.execute("SELECT * FROM location LIMIT 10;")
        rows = self.cursor.fetchall()
        return[Location(*row) for row in rows]
