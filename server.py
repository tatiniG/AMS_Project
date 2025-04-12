from flask import Flask, jsonify, send_from_directory
from controllers.controller import Controller
from views.view import View
import os

app = Flask(__name__, static_folder='website')
controller = Controller(View())

@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/website/<path:path>')
def serve_static_file(path):
    return send_from_directory(app.static_folder, path)

@app.route('/api/patients')
def get_patients():
    patients = controller.get_all_patients()
    return jsonify([vars(p) for p in patients])

@app.route('/api/locations')
def get_hospitals():
    locations = controller.get_all_locations()
    return jsonify([vars(l) for l in locations])

if __name__ == '__main__':
    app.run(debug=True)
