from utils import load_data, save_data

# Add Student
def add_student():
    data = load_data()
    try:
        roll = int(input("Enter Roll No: "))
        name = input("Enter Name: ")
        marks = float(input("Enter Marks: "))

        student = {"roll": roll, "name": name, "marks": marks}
        data.append(student)

        save_data(data)
        print("Student added successfully!")

    except ValueError:
        print("Invalid input! Please enter correct data.")

# View Students
def view_students():
    data = load_data()
    if not data:
        print("No records found.")
        return

    for s in data:
        print(s)

# Search Student
def search_student():
    data = load_data()
    try:
        roll = int(input("Enter Roll No to search: "))
        for s in data:
            if s["roll"] == roll:
                print("Student found:", s)
                return
        print("Student not found.")
    except ValueError:
        print("Invalid input!")

# Update Student
def update_student():
    data = load_data()
    try:
        roll = int(input("Enter Roll No to update: "))
        for s in data:
            if s["roll"] == roll:
                s["name"] = input("Enter new name: ")
                s["marks"] = float(input("Enter new marks: "))
                save_data(data)
                print("Student updated!")
                return
        print("Student not found.")
    except ValueError:
        print("Invalid input!")

# Delete Student
def delete_student():
    data = load_data()
    try:
        roll = int(input("Enter Roll No to delete: "))
        new_data = [s for s in data if s["roll"] != roll]

        if len(data) == len(new_data):
            print("Student not found.")
        else:
            save_data(new_data)
            print("Student deleted!")

    except ValueError:
        print("Invalid input!")

# Sort Students
def sort_students():
    data = load_data()
    choice = input("Sort by (name/marks): ").lower()

    if choice == "name":
        data.sort(key=lambda x: x["name"])
    elif choice == "marks":
        data.sort(key=lambda x: x["marks"], reverse=True)
    else:
        print("Invalid choice!")
        return

    for s in data:
        print(s)

# Reports
def generate_report():
    data = load_data()
    if not data:
        print("No data available.")
        return

    topper = max(data, key=lambda x: x["marks"])
    avg = sum(s["marks"] for s in data) / len(data)

    print("\n--- Report ---")
    print("Topper:", topper)
    print("Average Marks:", avg)