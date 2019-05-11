class Person:
    name = ""
    age = 0
    sex = ""
    __weight = 50

    def __init__(self, name, age):
        self.name = "NBAI-" + name
        self.age = age

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name + "."

    def __str__(self):
        return "Name: %s, Age: %d " % (self.name, self.age)


class Student(Person):
    role = "Student"

    def set_name(self, name):
        self.name = name+"."

    def __str__(self):
        return "Name: %s, Age: %d role %s" % (self.name, self.age, self.role)


class Teacher(Person):
    role = "Teacher"

    def __str__(self):
        return "Name: %s, Age: %d role %s" % (self.name, self.age, self.role)


if __name__ == "__main__":
    jim = Student("Jim", 20)
