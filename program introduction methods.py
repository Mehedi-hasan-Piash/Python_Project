class Student :
    roll = ""
    name = ""
    age = ""
    cgpa = ""

    def set_Value(self, roll, name, age, cgpa):
        self.roll = roll
        self.name = name
        self.age = age
        self.cgpa = cgpa

    def display (self) :
        print(f"Roll : {self.roll}, Name : {self.name}, Age : {self.age}, CGPA : {self.cgpa}")

tazmal = Student()
tazmal.set_Value(101, "Tazmal", 35, 3.55)
tazmal.display()

rifat = Student()
rifat.set_Value(102, "Rifat", 27, 3.75)
rifat.display()

rasel = Student()
rasel.set_Value(103, "Rasel", 34, 3.70)
rasel.display()

piash = Student()
piash.set_Value(104, "Piash", 23, 3.67)
piash.display()



























