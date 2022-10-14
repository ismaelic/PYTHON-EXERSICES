objetive = int(input('Escoge un numero: '))
epsilon = 0.01
step = epsilon**2
answer = 0.0

while abs(answer**2 - objetive) >= epsilon and answer <= objetive:
    answer += step


if abs(answer**2 - objetive) >= epsilon:
    print(f'No se encontro la raiz cuadrada de {objetive}')
else:
    print(f'La raiz cuadrada de {objetive} es {answer}')
