class intro:

    def __init__(self , name, occupation):
        print("Hey, I am Constructor.")
        self.name = name
        self.occ = occupation

    def info(self):
        print(f"{self.name} is a {self.occ}.")

a = intro("Ravi", "Developer")
a.info()
b = intro("Pawan", "Boy")
b.info()
c = intro("Sandeep", "Anaconda")
c.info()