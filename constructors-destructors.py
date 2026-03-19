class student:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
        print(f"Student {name} created")

    
    def __del__(self):
            print(f"Student {self.name} destroyed")
student1 = student("Nancy", 20, "nancy027@gmail.com")
print(student1.name)
print(student1.age)
print(student1.email)
del student1