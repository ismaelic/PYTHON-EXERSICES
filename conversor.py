def process(type_coin, dollar_value):
    coin = float(input('¿Cuántos pesos ' + type_coin + ' tienes?'))

    dollars = round(coin / dollar_value)
    dollars = str(dollars)

    print('Tienes $ ' + dollars + 'dólares')


menu = """
  Bienvenido al conversor de monedas

  1 - Pesos colombianos
  2 - Pesos argentinos
  3 - Pesos mexicanos

  Elige una opcion:
"""

option = float(input(menu))

if option == 1:
    process('colombianos', 3500)

elif option == 2:
    process('argentinos', 65)

elif option == 3:
    process('mexicanos', 24)
else:
    print('Ingresa una opción valida, por favor')
