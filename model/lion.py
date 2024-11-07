from model.breathe_able import Breathe_Able
from model.swim_able import Swim_Able
from model.terrestrial_able import Terrestrial_Able


class Lion(Breathe_Able,Swim_Able,Terrestrial_Able):
    def breathe(self):
        print("Breathe")
    def swim(self):
        print("Hidratarse ")
    def terrestrial(self):
        print("Terrestrial sabana")