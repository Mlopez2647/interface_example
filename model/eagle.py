from model.breathe_able import Breathe_Able
from model.fly_able import Fly_Able
from model.terrestrial_able import Terrestrial_Able


class Eagle(Breathe_Able,Fly_Able, Terrestrial_Able):
    def breathe(self):
        print("Aire fresco")
    def fly(self):
        print("Vuela alto")
    def terrestrial(self):
        print("camina poco")