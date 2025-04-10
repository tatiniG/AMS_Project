from views.view import View
from controllers.controller import Controller

if __name__ == "__main__":
    view = View()
    controller = Controller(view)

    controller.create_hospital("General Hospital", "New York", "NY")