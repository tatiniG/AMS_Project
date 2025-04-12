class Hospital:
    def __init__(self, object_id, name, address, city, state, zip_code, telephone, type_, status, county, country, latitude, longitude, owner, helipad):
        self.object_id = object_id
        self.name = name
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.telephone = telephone
        self.type = type_
        self.status = status
        self.county = county
        self.country = country
        self.latitude = latitude
        self.longitude = longitude
        self.owner = owner
        self.helipad = helipad

    def __str__(self):
        return f"Hospital({self.name}, {self.city}, {self.state})"