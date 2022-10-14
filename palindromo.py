def palindrome(work):
    work = work.replace(' ', '').lower()
    inverted_work = work[::-1]
    if work == inverted_work:
        return True
    else:
        return False


def run():
    work = input('Escribe una palabra: ')
    is_palindrome = palindrome(work)
    if is_palindrome == True:
        print('Es palindromo')
    else:
        print('No es palindromo')


if __name__ == '__main__':
    run()
