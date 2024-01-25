class Student :
    roll = ""
    name = ""
    age = ""
    cgpa = ""

    def __init__ (self, roll, name, age, cgpa) :
        self.roll = roll
        self.name = name
        self.age = age
        self.cgpa = cgpa

    def display (self) :
        print(f"Roll : {self.roll}, Name : {self.name}, Age : {self.age}, CGPA : {self.cgpa}")

tazmal = Student(101, "Tazmal", 35, 3.55)
tazmal.display()

rifat = Student(102, "Rifat", 27, 3.75)
rifat.display()

rasel = Student(103, "Rasel", 34, 3.70)
rasel.display()

piash = Student(104, "Piash", 23, 3.67)
piash.display()



























