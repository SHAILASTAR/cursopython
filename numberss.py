"""
# TIPOS DE DATOS
10
14.4 #dato flotante

print(type(9)) # pondra <<class 'int'>>, hace referencia a un numero entero
print(type(10.1)) # pondra <<class 'float'>>, hacer referencia a un numero flotante

print(1 + 1)

# OPERACIONES EN EL CMD
1 + 1 = 2   # suma
2 - 1 = 1   # resta
-3 + 2 = -1
1 + 1.0 = 2.0
1 * 2.0 = 2.0   # multi
2**3 = 8    # 2 elevado a 3
3 / 2 = 1.5     # division
3 // 2 = 1     # parte entera del residuo de la division
3 % 2 = 1   # operador de modulo (residuo)
10 % 3 = 1
20 - 10 / 5 * 3**2 = 2.0    # tabla de presidencia
(20 - 10) / (5 * 3**2) = 0.2222222222222222
"""

age = input("Insert your age: ")
new_age = int(age) + 5  # el 'int' convierte la age en un numero
print(new_age)  # suma la age mas 5, si en el cmd insertamos que la edad es 10 entonces sumara 10 + 5 (solo se pueden poner numeros)