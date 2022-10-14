objetive = int(input('Escoge un numero: '))
epsilon = 0.01
lower_limit = 0.0
upper_limit = max(1.0, objetive)
answer = (upper_limit + lower_limit) / 2


while abs(answer**2 - objetive) >= epsilon:
    if answer**2 < objetive:
        lower_limit = answer
    else:
        upper_limit = answer

    answer = (upper_limit + lower_limit) / 2

print(f'La raiz cuadrada de {objetive} es {answer}')
