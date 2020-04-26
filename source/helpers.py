import random
from .. import settings

class GenericNode:
    def __init__(self, root_value=None):
        self.root = root_value
        self.num_child = 0
        self.energy = self.define_energy()

        self.increment_father()

    def increment_father(self):
        if self.root != None:
            self.root.num_child += 1

    def define_energy(self):
        return random.randint(settings.MIN_VALUE_ENERGY, settings.MAX_VALUE_ENERGY)
