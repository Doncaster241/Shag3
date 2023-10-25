import random


class Zoo:
    group1 = "Mammals"
    group2 = "Birds"

    def __init__(self, name = "Tiger"):
        self.name=name
        self.paws = 4
        self.swimming = True
        self.wings = 0
        self.flying = False

    def __init__(self, name="Penguin"):
        self.name = name
        self.paws = 2
        self.swimming = True
        self.wings = 2
        self.flying = False


    def __init__(self, name="Parrot"):
        self.name = name
        self.paws = 2
        self.swimming = False
        self.wings = 2
        self.flying = True

    def __init__(self, name="Porcupine"):
        self.name = name
        self.paws = 4
        self.swimming = True
        self.wings = 0
        self.flying = False


print("write 1 if you want Tiger")
print("write 2 if you want Penguin")
print("write 3 if you want Parrot")
print("write 4 if you want Porcupine")

T = int(input())
if T == 1:
    print("Tiger can't fly and can swim, but don't like it")
elif T == 2:
    print("Penguin can't fly and can swim, it's very shy")
elif T == 3:
    print("Parrot can fly, but can't swim, it's very shy")
elif T == 4:
    print("Porcupine can't fly and can swim, but it has spines")


class Auto:
    Brand = "Audi"
    model = "A6"

    def __init__(self, name):
        self.name=name
        self.speed = 50
        self.warning = 10
        self.working = True

    def A(self):
        print("Steel working")
        self.speed += 15
        self.self.warning -= 2

    def B(self):
        print("Good working")
        self.speed += 30
        self.self.warning -= 3.5

    def C(self):
        print("A bit worse working")
        self.speed += 3
        self.self.warning -= 0.1

    def D(self):
        print("Bad working")
        self.speed -= 5
        self.self.warning += 1

    def E(self):
        print("Very bad working")
        self.speed -= 10
        self.self.warning += 2

    def arrived(self):
        print(f"Speed = {self.speed}")
        print(f"Warning = {self.warning}")

    def Aut(self):
        G = random.randint(1, 4)
        if G == 1:
            self.A()
        if G == 2:
            self.B()
        if G == 3:
            self.C()
        if G == 4:
            self.E()

    def end(self):
        if self.speed > 80:
            print('So speed')
            self.working = False
        if self.speed < 80:
            self.working = False
            print('So so')
        elif self.warning > 1:
            self.working = False
            print('Dont working')

H = Auto(name = "Audi A6")
for i in range(365):
    if H.working == False:
        break
    H.Aut(i)