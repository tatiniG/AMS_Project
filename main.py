from views.view import View
from controllers.controller import Controller

if __name__ == "__main__":
    view = View()
    controller = Controller(view)

    patients = controller.get_all_patients()
    for patient in patients:
        print(patient)
    
    hospitals = controller.get_all_locations()
    for hospital in hospitals:
        print(hospital)