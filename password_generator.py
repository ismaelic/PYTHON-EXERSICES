import random


def pass_generator():
    uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G',
                 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T',
                 'U', 'V', 'W', 'X', 'Y', 'Z']
    lowercase = ['a', 'b', 'c', 'd', 'e', 'f',
                 'g', 'h', 'i', 'j', 'k', 'l',
                 'm', 'n', 'ñ', 'o', 'p', 'q',
                 'r', 's', 't', 'u', 'v', 'w',
                 'x', 'y', 'z']
    sym = ['!', '#', '%', '(', ')']
    number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    characters = uppercase + lowercase + sym + number

    password = []

    for i in range(15):
        character_random = random.choice(characters)
        password.append(character_random)

    password = ''.join(password)
    return password


def run():
    password = pass_generator()
    print('Tu nueva contraseña es: ' + password)


if __name__ == '__main__':
    run()
