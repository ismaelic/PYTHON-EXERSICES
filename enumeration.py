objetive = int(input('Escoge un entero: '))
answer = 0

while answer ** 2 < objetive:
    print(answer)
    answer += 1


if answer ** 2 == objetive:
    print(f'La raiz cuadrada de {objetive} es {answer}')
else:
    print(f'{objetive} no tiene una raiz cuadrada entera')
