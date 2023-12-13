
lista = ["a", "b", "c", "d", "e", "a"]
nuevo = set(lista)
print(lista)

#Funcionalidades especiales
#Ordenar lista alfanuméricamente
nombre_lista = [2,3,4,5]
nueva_lista = nombre_lista.sort()
#Ordenar lista descendiente
nombre_lista = [2,3,4,5]
nueva_lista = nombre_lista.sort(reverse = True)
#Ordenar la lista al revés
nombre_lista = ["banana", "Orange", "Kiwi", "cherry"]
nombre_lista .reverse()
#Ordenar lista sin que afecte las mayúsculas
nombre_lista = ["banana", "Orange", "Kiwi", "cherry"]
nombre_lista .sort(key = str.lower)
#Copiar una lista
nombre_lista = [1,2,3,4,5,6,7,8,9]
copia = nombre_lista.copy()
#Unir lista
lista1 = ["a","b","c"]
lista2 = [1,2,3]

lista3 = lista1 + lista2 
#Remover datos duplicados
nombre_lista = ["a","a","b","c"]

nueva = sorted(set(nombre_lista))
#Agregar lista
#append
#Los datos agregados quedaran en la parte final de la lista
nombre_lista = [1,2,3]
nombre_lista.append(4)
#insert
#los datos segregaran dependiendo de la función
nombre_lista = [1,2,3]
nombre_lista.insert(1,9)
#extend
#esto permite crear una lista nueva y agregar a a la ya creada
nombre_lista = [1,2,3]
nombre_lista.extend([4,5,6,7])
#Limpiar Lista
nombre_lista = [1,2,3]
nombre_lista.clear()