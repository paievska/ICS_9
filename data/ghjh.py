class Girls:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Girls = (self.name)"  

a = Girls('Mary', 20) 
print(a.age)  