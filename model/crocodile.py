from model.breathe_able import Breathe_Able
from model.swim_able import Swim_Able
from model.terrestrial_able import Terrestrial_Able


class Crocodile(Swim_Able,Terrestrial_Able,Breathe_Able):
    def swim(self):
        print("Nada por horas")
    def breathe(self):
        print("Respira")
    def terrestrial(self):
        print("solo se arrastra")