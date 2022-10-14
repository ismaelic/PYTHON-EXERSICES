def run():
    # for counter in range(1000):
    #     if counter % 2 != 0:
    #         continue
    #     print(counter)

    text = input('Escribe un texto: ')
    for letter in text:
        if letter == 'o':
            break
        print(letter)


if __name__ == '__main__':
    run()
