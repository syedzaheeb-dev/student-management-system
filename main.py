import json
import os

FILE_NAME = "students.json"


class Student:
    def __init__(self, name: str, age: int, grade: str):
        self.name = name
        self.age = age
        self.grade = grade

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "grade": self.grade
        }


class StudentManager:
    def __init__(self):
        self.students = self._load_students()

    def _load_students(self):
        if not os.path.exists(FILE_NAME):
            return []

        try:
            with open(FILE_NAME, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []

    def _save_students(self):
        with open(FILE_NAME, "w") as f:
            json.dump(self.students, f, indent=4)

    def add_student(self, name, age, grade):
        if any(s["name"].lower() == name.lower() for s in self.students):
            print("Student already exists.")
            return

        student = Student(name, age, grade)
        self.students.append(student.to_dict())
        self._save_students()
        print("Student added successfully.")

    def remove_student(self, name):
        updated_students = [
            s for s in self.students
            if s["name"].lower() != name.lower()
        ]

        if len(updated_students) == len(self.students):
            print("Student not found.")
            return

        self.students = updated_students
        self._save_students()
        print("Student removed successfully.")

    def search_student(self, name):
        for s in self.students:
            if s["name"].lower() == name.lower():
                print(f"Found: {s['name']} | Age: {s['age']} | Grade: {s['grade']}")
                return

        print("Student not found.")

    def show_all(self):
        if not self.students:
            print("No students available.")
            return

        for i, s in enumerate(self.students, start=1):
            print(f"{i}. {s['name']} | Age: {s['age']} | Grade: {s['grade']}")


def menu():
    manager = StudentManager()

    actions = {
        "1": "Add Student",
        "2": "Remove Student",
        "3": "Search Student",
        "4": "Show All Students",
        "5": "Exit"
    }

    while True:
        print("\n--- Student Management System ---")
        for key, value in actions.items():
            print(f"{key}. {value}")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            name = input("Name: ").strip()
            age = input("Age: ").strip()
            grade = input("Grade: ").strip()
            manager.add_student(name, age, grade)

        elif choice == "2":
            name = input("Enter name to remove: ").strip()
            manager.remove_student(name)

        elif choice == "3":
            name = input("Enter name to search: ").strip()
            manager.search_student(name)

        elif choice == "4":
            manager.show_all()

        elif choice == "5":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    menu()