import random


def run():
    random_number = random.randint(1, 100)
    chosen_number = int(input('Elige un numero del 1 al 100: '))
    while chosen_number != random_number:
        if chosen_number < random_number:
            print('El numero es mas grande')
        else:
            print('El numero es mas pequeño')
        chosen_number = int(input('Elige otro numero: '))
    print('Ganaste')


if __name__ == '__main__':
    run()
