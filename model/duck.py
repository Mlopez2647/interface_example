from model.breathe_able import Breathe_Able
from model.fly_able import Fly_Able
from model.swim_able import Swim_Able
from model.terrestrial_able import Terrestrial_Able


class Duck(Fly_Able,Breathe_Able,Terrestrial_Able,Swim_Able):
    def fly(self):
        print("Flying")
    def swim(self):
        print("Swiming")
    def breathe(self):
        print("Breathing")
    def terrestrial(self):
        print("Terrestrial")