class interview:
    name = 'Ravi'
    occupation = 'fresher'
    language = 'python'
    def info(self):
        print(f"{self.name} is a {self.occupation}. He knows {self.language}.")

pawan = interview()
sandeep = interview()
anoop = interview()
ravi = interview()

pawan.name = "Pawan"
pawan.occupation = "Software Engineer"
pawan.language = "Java"

sandeep.name = "Sandeep"
sandeep.occupation = "Mechanical Engineer"
sandeep.language = "Javascript"

anoop.name = "Anoop"
anoop.occupation = "Web Developer"
anoop.language = "C++"

pawan.info()
sandeep.info()
anoop.info()
ravi.info()