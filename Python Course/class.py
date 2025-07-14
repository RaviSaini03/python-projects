class intro:
    name = 'Ravi'
    occupation = 'Bussines Man'
    def info(self):
        print(f"{self.name} is a {self.occupation}.")

a = intro()
b = intro()
c = intro()
d = intro()

a.name = 'Pawan'
a.occupation = 'CEO of Google'

b.name = 'Sandeep'
b.occupation = 'CTO of Samsung'

c.name = 'Priyanshu'
c.occupation = 'Rocket Scientist'

a.info()
b.info()
c.info()
d.info()