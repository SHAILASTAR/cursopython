demo_list = [1, 'hello', 1.34, True, [1, 2, 3]]
colors = ['red', 'green', 'blue']

numbers_list = list((1, 2, 3, 4))   # parentesis rosa es una tupla dentro de la lista, para que salgan los 4 numeros, si se uita el parentesis rosa entonces saldra error
#print(numbers_list) # lo imprime normal
#print((type(numbers_list)) # para saber el tipo de dato, en este caso 'list'

#r = list(range(1, 10))  # para crear una lista que salgan todos los numeros del 1 al 9 porque siempre sale un valor menos en el cmd
#print(r)

#print(type(colors))
#print(dir(colors))  # muestra informacion de lo que puedes hacer con una lista
#print(len(demo_list))  # muestra el numero de elementos que hay en la lista
#print(colors[1])     # muestra la posicion de el elemento que le indiquemos de la lista
#print('green' in colors)    # para saber si 'green' esta en la lista de colors, saldra true en este caso

#print(colors)
#colors[1] = 'yellow'    # cambia el 1 (que es el green el la lista de colors) por 'yellow'
#print(colors)

#print(dir(colors))

#colors.append('violet')     # .append: para añadir un elemento mas a la lista, en este caso 'violet' (solo se puede un elemento mas)
#colors.extend(['violet', 'yellow'])   # se podran añadir mas de 1 elemento a la lista sin que esten dentro de una tupla
#colors.extend(['pink', 'black'])

#colors.insert(1, 'violet')  # insertara 'violet' justo despues de 'red'
#colors.insert(len(colors), 'violet')

#print(colors)

#colors.pop()    # quita el ultimo elemento de la lista añadido
#colors.pop()    # si lo añadimos 2 veces entonces quitara 2 elementos de la lista
#colors.remove('green')  # quita el elemento que quieres
#colors.pop(1)   # quita el elemento que quieres
#colors.clear()  # elimina todos los elementos de la lista

#colors.sort()   # ordena la lista alfabeticamente
#colors.sort(reverse=True)    #ordena la lista alfebeticamente del reves, de la Z a la A

print(colors)

print(colors.index('blue'))

