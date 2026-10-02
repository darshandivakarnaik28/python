#hospital management system using OOP concepts
from abc import ABC, abstractmethod
class Person(ABC):
    def __init__(self, name: str, age: int, gender: str, mobno: str):
        self.name = name
        self.age = age
        self.gender = gender
        self.mobno = mobno

    @abstractmethod
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Mobile Number: {self.mobno}")


class Doctor(Person):
    def __init__(self, name: str, age: int, gender: str, specialization: str, mobno: str):
        super().__init__(name, age, gender, mobno)
        self.specialization = specialization
        self.is_available = True

    def display_info(self):
        print(f"--- Dr. {self.name} ({self.specialization}) ---")
        super().display_info()
        print(f"Availability Status: {'Available' if self.is_available else 'Busy'}")

    def generate_patient_report(self, patient, diagnosis: str, prescription: str):
        report = f"Diagnosis: {diagnosis} | Prescription: {prescription} | Attending: Dr. {self.name}"
        patient.add_medical_record(report)
        return report


class Patient(Person):
    def __init__(self, name: str, age: int, gender: str, problem: str, mobno: str):
        super().__init__(name, age, gender, mobno)
        self.problem = problem
        self.__medical_records = []

    def add_medical_record(self, record: str):
        self.__medical_records.append(record)

    def view_history(self):
        print(f"\n--- Medical History for {self.name} ---")
        print(f"Current Complaint: {self.problem}")
        if not self.__medical_records:
            print("No previous medical reports found.")
        else:
            for i, record in enumerate(self.__medical_records, 1):
                print(f" Record #{i}: {record}")

    def display_info(self):
        print(f"--- Patient: {self.name} ---")
        super().display_info()
        print(f"Primary Problem: {self.problem}")


class Appointment:
    _id_counter = 1001
    def __init__(self, doctor: Doctor, patient: Patient, date: str, time: str):
        self.appointment_id = Appointment._id_counter
        Appointment._id_counter += 1
        self.doctor = doctor
        self.patient = patient
        self.date = date
        self.time = time
        self.status = "Scheduled"
        self.doctor.is_available = False

    def cancel(self):
        self.status = "Cancelled"
        self.doctor.is_available = True
        print(f"Appointment ID {self.appointment_id} for {self.patient.name} has been cancelled.")

    def display_details(self):
        print(
            f"Appt ID: {self.appointment_id} | Patient: {self.patient.name} | "
            f"Doctor: Dr. {self.doctor.name} ({self.doctor.specialization}) | "
            f"Date/Time: {self.date} at {self.time} | Status: {self.status}"
        )


class Hospital:
    def __init__(self, name: str, address: str):
        self.name = name
        self.address = address
        self.doctors = []
        self.patients = []
        self.appointments = []

    def add_doctor(self, doctor: Doctor):
        self.doctors.append(doctor)
        print(f"Dr. {doctor.name} added to {self.name}.")

    def add_patient(self, patient: Patient):
        self.patients.append(patient)
        print(f"Patient {patient.name} added to system.")

    def view_available_doctors(self):
        print("\n--- Available Doctors ---")
        available = [doc for doc in self.doctors if doc.is_available]
        if not available:
            print("No doctors currently available.")
        for doc in available:
            print(f"- Dr. {doc.name} [{doc.specialization}]")

    def display_doctor_schedules(self):
        print("\n--- Doctor Schedules & Status ---")
        for doc in self.doctors:
            status = "Available" if doc.is_available else "Booked"
            print(f"Dr. {doc.name} ({doc.specialization}): {status}")

    def book_appointment(self, patient_name: str, doctor_name: str, date: str, time: str):
        patient = next((p for p in self.patients if p.name == patient_name), None)
        doctor = next((d for d in self.doctors if d.name == doctor_name and d.is_available), None)

        if not patient:
            print(f"Error: Patient '{patient_name}' not found.")
            return None
        if not doctor:
            print(f"Error: Dr. '{doctor_name}' is not available or not found.")
            return None

        appt = Appointment(doctor, patient, date, time)
        self.appointments.append(appt)
        print(f"Appointment successfully booked for {patient.name} with Dr. {doctor.name}.")
        return appt

    def cancel_appointment(self, appointment_id: int):
        appt = next((a for a in self.appointments if a.appointment_id == appointment_id and a.status == "Scheduled"), None)
        if appt:
            appt.cancel()
        else:
            print(f"Active appointment with ID {appointment_id} not found.")

if __name__ == "__main__":
    city_hospital = Hospital("City Hospital", "123 Main St")
    doc1 = Doctor("Smith", 45, "Male", "Cardiology", "0987654321")
    doc2 = Doctor("Johnson", 38, "Female", "Dermatology", "1234567890")
    
    pat1 = Patient("Alice", 30, "Female", "Flu", "1234567890")
    pat2 = Patient("Bob", 25, "Male", "Skin Rash", "0987654321")

    city_hospital.add_doctor(doc1)
    city_hospital.add_doctor(doc2)
    city_hospital.add_patient(pat1)
    city_hospital.add_patient(pat2)

    city_hospital.view_available_doctors()

    print("\n--- Booking Appointments ---")
    appt1 = city_hospital.book_appointment("Alice", "Smith", "2026-08-10", "10:00 AM")

    city_hospital.display_doctor_schedules()

    print("\n--- Generating Reports ---")
    if appt1:
        doc1.generate_patient_report(pat1, "Viral Infection", "Rest and Hydration")

    pat1.view_history()

    print("\n--- Cancelling Appointment ---")
    if appt1:
        city_hospital.cancel_appointment(appt1.appointment_id)

    city_hospital.display_doctor_schedules()
