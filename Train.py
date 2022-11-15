import random as rand

class train:
    def __init__(self):
        self.front = None
    
    def print_train(self):
        self.front.printall

class traincar:
    def __init__(self):
        self.id: int = rand.randint(100, 999)
        self.back: traincar = None
        self.is_full: bool = False

    def printall(self):
        self.print()
        if self.back:
            self.back.printall()

    def print(self):
        pass

class locomotive(traincar):
    def __init__(self, horn_length, horn_frequency):
        super.__init__()
        self.horn_length = horn_length
        self.horn_frequency = horn_frequency

    def print(self):
        if self.back:
            print(f"I am a Locomotive, my ID is {self.id}, and there is a care behind me")

    def honk(self):
        pass

class freightcar(traincar):
    def __init__(self, freight_type):
        super.__init__()
        self.freight_type: str = freight_type
