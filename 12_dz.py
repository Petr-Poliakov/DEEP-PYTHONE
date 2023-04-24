
import csv

class NameDescriptor:
    def __set__(self, instance, value):
        if not value.istitle() or not value.isalpha():
            raise ValueError("Invalid name")
        else:
            instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name

class Subject:
    def __init__(self, name):
        self.name = name
        self.marks = []
        self.tests = []

    def add_mark(self, mark):
        if mark < 2 or mark > 5:
            raise ValueError("Invalid mark")
        self.marks.append(mark)

    def add_test(self, test):
        if test < 0 or test > 100:
            raise ValueError("Invalid test score")
        self.tests.append(test)

    def average_mark(self):
        if not self.marks:
            return 0
        return sum(self.marks) / len(self.marks)

    def average_test_score(self):
        if not self.tests:
            return 0
        return sum(self.tests) / len(self.tests)

class Student:
    name = NameDescriptor()

    def __init__(self, name, subjects_file):
        self.name = name
        self.subjects = {}
        self.load_subjects(subjects_file)

    def load_subjects(self, subjects_file):
        with open(subjects_file) as f:
            reader = csv.reader(f)
            for row in reader:
                name, *_ = row
                if name not in self.subjects:
                    self.subjects[name] = Subject(name)
                else:
                    raise ValueError("Multiple entries for subject {}".format(name))

    def add_mark(self, subject_name, mark):
        if subject_name not in self.subjects:
            raise ValueError("Invalid subject")
        self.subjects[subject_name].add_mark(mark)

    def add_test(self, subject_name, test):
        if subject_name not in self.subjects:
            raise ValueError("Invalid subject")
        self.subjects[subject_name].add_test(test)

    def average_subject_marks(self):
        total_marks = 0
        num_subjects = 0
        for subject in self.subjects.values():
            total_marks += subject.average_mark()
            num_subjects += 1
        return total_marks / num_subjects

    def __str__(self):
        return "Student {}: {}".format(self.name, ", ".join(self.subjects.keys()))


with open("subjects.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Subject", "Grade"])
    writer.writerow(["Math", 4])
    writer.writerow(["Math", 5])
    writer.writerow(["Math", 80])
    writer.writerow(["Math", 90])
    writer.writerow(["English", 3])
    writer.writerow(["English", 4])
    writer.writerow(["English", 70])
    writer.writerow(["English", 80])

s = Student("Alex", "subjects.csv")
# s.add_mark("Math", 4)
# s.add_mark("Math", 5)
# s.add_test("Math", 80)
# s.add_test("Math", 90)
# s.add_mark("English", 3)
# s.add_mark("English", 4)
# s.add_test("English", 70)
# s.add_test("English", 80)
print(s)
print("Math average mark:", s.subjects["Math"].average_mark())
# print("Math average test score:", s.subjects["Math"].average_test_score())
# print("English average mark:", s.subjects["English"].average_mark())
# print("English average test score:", s.subjects["English"].average_test_score())
# print("Overall average mark:", s.average_subject_marks())
