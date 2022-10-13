#PRINCIPIOS SOLID EN PYTHON
#los principios solid buscan que el codigo sea mantenible
#
    
    #S  el principio de responsabilidad unica
    #O  el principio de abierto cerrado
    #L  principio de sustitucion de liskov
    #I  principio de segregacion de interfaces
    #D  principio de inversion de dependencias
    

#no necesariamente es un ´paso paso y no siempres eutilizan todos

#S  el principio de responsabilidad unica
#busca que un codio tenga una unica responsabilidad es decir que un codigo solo cumpla una funcion

#SIN RESPONSABILIDAD UNICA
def get_num_and_bigger(list_of_items):
    list_of_numbers = []

    #crea una lista de solo numeros
    for item in list_of_items:
        if isinstance(item, int):
            list_of_numbers.append(item)
    print(list_of_numbers)
    #encuentra el mayor numero
    bigger_number = max(list_of_numbers)
    print(bigger_number)

print(get_num_and_bigger([1, 2, "pepe", 9, 10, 6, 7, 8]))


#resolvamos este problema aplicando el principio de responsabilidad unica

def get_only_numbers(list_of_items):
    """Esta funcion me crea una lista donde sus unicos elementos son numeros

    Args:
        list_of_items (_type_): lista de items 

    Returns:
        _type_: valor máximo de la lista
    """
    list_of_numbers = []

    #crea una lista de solo numeros
    for item in list_of_items:
        if isinstance(item, int):
            list_of_numbers.append(item)
    return list_of_numbers
#lo anterior es muy util porque lo que buscamos con python es no repetir , principio DRY "no repitas" 
#asi conn esta misma funcion la podemos utilizar despues 

def get_max_value(list_numbers):
    max_value = max(list_numbers)
    return max_value


def run(list_of_items):
    list_numbers = get_only_numbers(list_of_items)
    max_value = get_max_value(list_numbers)
    return max_value


print(run([1, 2, "pepe", 9, 10, 6, 7, 8]))
print(get_only_numbers([1, 2, "pepe", 9, 10, 6, 7, 8]))