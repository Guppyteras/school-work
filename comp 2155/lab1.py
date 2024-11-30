import argparse

class Student:
    def __init__(self, firstname, lastname, student_id):
        self.firstname = firstname
        self.lastname = lastname
        self.student_id = student_id

    def __str__(self):
        return f"The student with id of {self.student_id} is named {self.lastname}, {self.firstname}"

    def write_to_file(self):
        filename = f"{self.student_id}.txt"
        with open(filename, 'w') as file:
            file.write(f"{self.firstname} {self.lastname}")
        print(f"Student information written to {filename}")

def main():
    parser = argparse.ArgumentParser(description='Process student information.')
    parser.add_argument('firstname', type=str, help='First name of the student')
    parser.add_argument('lastname', type=str, help='Last name of the student')
    parser.add_argument('student_id', type=str, help='Student ID')

    args = parser.parse_args()

    # Create Student instance
    student = Student(args.firstname, args.lastname, args.student_id)

    # Write student information to file
    student.write_to_file()

    # Output student summary to screen
    print(student)

if __name__ == '__main__':
    main()