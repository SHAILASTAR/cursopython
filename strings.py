myStr = "Hello World"

#print(dir(myStr))

# print(myStr.upper()) # .upper: convierte el string en mayuscula
# print(myStr.lower()) # .lower: convierte el string en minuscula
# print(myStr.swapcase()) # .swapcase: convierte una letra minuscula en mayuscula y viceversa
# print(myStr.capitalize()) # .capitalize: convierte solo la primera letra de la palabra del string en mayuscula
# print(myStr.replace('Hello', 'bye')) # .replace: reemplaza una palabra del string por otra, antes de la coma (palabra que quieres reemplazar), despues de la coma (palabra que la sustituye)
# print(myStr.replace('Hello', 'bye').upper()) # Metodos encadenados
# print(myStr.count('l')) # .count: para contar algo del string, en este caso contamos las veces que esta la letra 'l' en el string

# print(myStr.startswith('hola')) # .startswith: para saber si el string escrito empieza por la palabra que hemos puesto, este caso 'hola' dara false
# print(myStr.startswith('Hello')) # en este caso dara true porque es la palabra que escribi en el string
# print(myStr.startswith('H')) # dara true porque el string empieza por 'H'
# print(myStr.endswith('World')) # dara true porque el string termina por 'World'
# print(myStr.endswith('world')) # dara false porque el string no termina por 'world'

# print(myStr.split('o')) # .split: divide el caracter del string, en cmd puede salir separado si el texto del string tiene principalmente un espacio en el string, tambien lo separa si dentro del parentesis le ponemos una letra entonces creara multiples elementos sin la letra que hayamos puesto (en este caso 'o')
# print(myStr.find('o')) # .find: para encontrar el numero de posicion de la letra 'o' del string, en este caso 'H'es posicion 0, 'e'es 1, 'l'es 2, 'l'es 3, 'o'es 4, tambien funciona con espacios

# print(len(myStr)) # len: para saber la longitud del string
# print(myStr.index('e')) # .index: para saber el indice de la letra 'e' que es 1 (no porque solo haya 1 'e', sino porque es su posicion)

# print(myStr.isnumeric()) # .isnumeric: para saber si el string es numerico
# print(myStr.isalpha()) # .
# (CONTROL+SHIFT+P+COMMENT = COMENTAR LO SELECCIONADO)

# print(myStr[0]) # para saber que letra esta en la posicion que indiquemos
# print(myStr[3])
# print(myStr[4])
# print(myStr[-1]) # si es un valor negativo, comenzara desde la derecha
# print(myStr[-5])


# JUNTAR DOS TEXTOS DE DIFERENTE MANERA (FUNCIONAN IGUAL):
print("My name is " + myStr) # suma de dos cosos
print(f"My name is {myStr}") # la 'f' es para que myStr haga la funcion de variable entre las llaves (para versiones 3.6 para arriba)
print("My name is {0}".format(myStr)) # para que se sepa que myStr va dentro de las llaves, 0 es la posicion