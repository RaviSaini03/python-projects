class intro:
    
    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    def show(self):
        print(f"Roll No. of {self.name} is {self.id}")

# When we need to change the name of the class or we can say that this same class will be copy in another class. because of this we use inheritence!!
class program(intro):
    def showLanguage(self):
        print("This is updated class because of inheritance.")

person1 = intro("Ravi Saini", "23ESGCS079")
person1.show()
person2 = program("Pawan Jangir", "23ESGCS069")
person2.show()
person2.showLanguage()