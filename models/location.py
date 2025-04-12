class Location:
    def __init__(self, id, city, state):
        self.id = id
        self.city = city
        self.state = state

    def __str__(self):
        return f"Location(city={self.city}, state={self.state})"