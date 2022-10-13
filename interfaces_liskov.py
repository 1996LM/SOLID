#el principio de sustitucion de liskov es que si tenemos una clase padre 
# y de esta tenemos clases hias , estas deben ser capaces de sustituir al padre y el codigo debe seguir 
#funcionando

#el principio de segregacion de interfaces
#las interfaces especificas del cliente son mejores que un ainterfas de proposito general 
#una interfas son esas clases que uno utiliza para representar las entidades importantes
#hay funciones que aunque no reportan herror , no tienen sentido

class Bird:
    def fly(self):
        return "I can fly"
    def walk(self):
        return "I can walk"
    
class Penguin(Bird):
    def fly(self):
        raise NotImplementedError("Cannot fly")


#con liskov y segregacion de interfaces

class BirdNew:
    def walk(self):
        return "I can walk"

class BirdCanFly(BirdNew):
    def fly(self):
        return "I can fly"

class PinguinNew(BirdNew):
    def walk(self):
        return super().walk()

class Duck(BirdCanFly):
    def fly(self):
        return super().fly()



