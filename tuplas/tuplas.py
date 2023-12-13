#Que son las tuplas
#Las tuplas son un tipo de lista, pero con la condición es que no se puede modificar y también consume menos recursos en memoria que la lista.
Mi_tuple = ("apple", "banana", "cherry")
print(Mi_tuple)
#Como acceder a una tupla
Mi_tuple = ("apple", "banana", "cherry")
print(Mi_tuple[1])
#Actualizar tupla
#las tuplas no se pueden modificar, pero si se puede convertir en una lista que si se pude modificar y después de modificarlo se puede convertir nueva mente en una tupla.
Mi_tuple = ("apple", "banana", "cherry")
Mi_lista = list(Mi_tuple)
Mi_lista[1] = "kiwi"
Mi_tuple = tuple(Mi_lista)
#Desempacar tuplas
#las tuplas se pueden desempacar y asignarse a una o varias variables 
Mi_tuple = ("apple", "banana", "cherry")
(green, yellow, red) = Mi_tuple
#si tienes mas en elementos en una tuplas  y tiene pocas variables a la ultima variable agrega *
Mi_tuple = ("apple", "banana", "cherry","raspberry")
(green, yellow, *red) = Mi_tuple
#Concatenar tuplas
#las tuplas se pueden concatenar, para que se pueden concatenar de hacer los siguiente.
Mi_tuple = ("apple", "banana", "cherry")
Mi_tupla2 = ("orange","raspberry")
Mi_tupla_conactenada = Mi_tuple + Mi_tupla2 
#Funciona Especial
#Count
#las función count permite saber cuantas veces existe elemento en la tupla
Mi_tuple = ("1", "3", "7", "8", "7", "5", "4", "6", "8", "5")
existe = Mi_tuple.count("5")
print(existe)