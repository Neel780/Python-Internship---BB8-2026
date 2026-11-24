class Bird:
    def fly(self):
        print("Bird is flapping its wings and flying.")

class Airplane:
    def fly(self):
        print("Airplane is soaring through the sky with jet engines.")

class Drone:
    def fly(self):
        print("Drone is hovering and flying with propellers.")

def make_it_fly(obj):
    obj.fly()

for flyer in [Bird(), Airplane(), Drone()]:
    make_it_fly(flyer)