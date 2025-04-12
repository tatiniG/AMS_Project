class Patient:
    def __init__(self, id, name, age, gender, blood_type, medical_condition, date_of_admission, doctor, hospital, insurance_provider, billing_amount, admission_type, discharge_date, medication, test_results):
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender
        self.blood_type = blood_type
        self.medical_condition = medical_condition
        self.date_of_admission = date_of_admission
        self.doctor = doctor
        self.hospital = hospital
        self.insurance_provider = insurance_provider
        self.billing_amount = billing_amount
        self.admission_type = admission_type
        self.discharge_date = discharge_date
        self.medication = medication
        self.test_results = test_results

    def __str__(self):
        return f"Patient({self.name}, {self.age}, {self.gender}, {self.medical_condition})"