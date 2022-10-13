#tiene que ver con el concepto de acoplamiento 
#es cuando dos estructuras se me acoplan para trabajar juntas
# esto no es bueno que pase. lo mejor es tener todo desacoplado
#porque cuando son acopladas si falla una fallan todas

#las abstracciones no deben depender de los detalles 
#los detalles deben depender de la abstraccion, los modulos de alto nivel no deben depender de los de menor nivel 


#EJEMPLO SIN INVERSION DE DEPENDENSIAS

class Engine(object):
    def __init__(self)-> None :
        pass

    def aceleracion():
        pass

    def getRPM(self):
        rpm_atual = 0
        return rpm_atual


class vehiculo():
    def __init__(self) -> None:
        self.engine = Engine

    def get_engine_rpm(self):
        return self.engine.getRPM()


#con inversion de dependencias

class Vehiculo():
    def __init__(self, engine) -> None:
        self._engine = engine

    def get_engine_rpm(self):
        return self._engine.getRPM()


vehiculo = Vehiculo(Engine())
print(vehiculo.get_engine_rpm())