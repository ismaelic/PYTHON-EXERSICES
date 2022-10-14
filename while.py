def run():
    LIMIT = 1000

    counter = 0

    operation_2 = 2**counter

    while operation_2 < LIMIT:
        print('2 elevado a ' + str(counter) +
              ' es igual a: ' + str(operation_2))
        counter += 1
        operation_2 = 2**counter


if __name__ == '__main__':
    run()
