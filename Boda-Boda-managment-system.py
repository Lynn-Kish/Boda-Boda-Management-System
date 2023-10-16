class BodaBodaCyclist:
    def __init__(self, name, age, address, contact, next_of_kin, next_of_kin_address, next_of_kin_contact, registration_no, stage):
        self.name = name
        self.age = age
        self.address = address
        self.contact = contact
        self.next_of_kin = next_of_kin
        self.next_of_kin_address = next_of_kin_address
        self.next_of_kin_contact = next_of_kin_contact
        self.registration_no = registration_no
        self.stage = stage

boda_boda_records = []

def register_boda_boda_cyclist():
    name = input("Name: ")
    age = input("Age: ")
    address = input("Address of Residence: ")
    contact = input("Contact: ")
    next_of_kin = input("Next of Kin Name: ")
    next_of_kin_address = input("Next of Kin Address: ")
    next_of_kin_contact = input("Next of Kin Contact: ")
    registration_no = input("Registration No. of Motorcycle: ")
    stage = input("Stage: ")
    
    cyclist = BodaBodaCyclist(name, age, address, contact, next_of_kin, next_of_kin_address, next_of_kin_contact, registration_no, stage)
    boda_boda_records.append(cyclist)
    print("Boda-Boda cyclist registered successfully.")

def show_registered_cyclists():
    for i, cyclist in enumerate(boda_boda_records, 1):
        print(f"\nCyclist {i}:")
        print(f"Name: {cyclist.name}")
        print(f"Age: {cyclist.age}")
        print(f"Address: {cyclist.address}")
        print(f"Contact: {cyclist.contact}")
        print(f"Next of Kin Name: {cyclist.next_of_kin}")
        print(f"Next of Kin Address: {cyclist.next_of_kin_address}")
        print(f"Next of Kin Contact: {cyclist.next_of_kin_contact}")
        print(f"Registration No. of Motorcycle: {cyclist.registration_no}")
        print(f"Stage: {cyclist.stage}")

def delete_record():
    registration_no = input("Enter Registration No. to delete: ")
    for cyclist in boda_boda_records:
        if cyclist.registration_no == registration_no:
            boda_boda_records.remove(cyclist)
            print("Record deleted successfully.")
            break
    else:
        print("No cyclist found with that Registration No.")

def edit_record():
    registration_no = input("Enter Registration No. to edit: ")
    for cyclist in boda_boda_records:
        if cyclist.registration_no == registration_no:
            cyclist.name = input(f"Name ({cyclist.name}): ") or cyclist.name
            cyclist.age = input(f"Age ({cyclist.age}): ") or cyclist.age
            cyclist.address = input(f"Address of Residence ({cyclist.address}): ") or cyclist.address
            cyclist.contact = input(f"Contact ({cyclist.contact}): ") or cyclist.contact
            cyclist.next_of_kin = input(f"Next of Kin Name ({cyclist.next_of_kin}): ") or cyclist.next_of_kin
            cyclist.next_of_kin_address = input(f"Next of Kin Address ({cyclist.next_of_kin_address}): ") or cyclist.next_of_kin_address
            cyclist.next_of_kin_contact = input(f"Next of Kin Contact ({cyclist.next_of_kin_contact}): ") or cyclist.next_of_kin_contact
            cyclist.stage = input(f"Stage ({cyclist.stage}): ") or cyclist.stage
            print("Record updated successfully.")
            break
    else:
        print("No cyclist found with that Registration No.")

while True:
    print("\nKampala Boda-Boda Management System")
    print("1. Register a New Boda-Boda Cyclist")
    print("2. Show Registered Boda-Boda Cyclists")
    print("3. Delete Records")
    print("4. Edit/Update Records")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        register_boda_boda_cyclist()
    elif choice == '2':
        show_registered_cyclists()
    elif choice == '3':
        delete_record()
    elif choice == '4':
        edit_record()
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please try again.")
