def division_elements_of_list(elements_list, divider):
    try:
        return [i / divider for i in elements_list]
    except ZeroDivisionError as error:
        return elements_list


element_list = list(range(10))
divider = 3

print(division_elements_of_list(element_list, divider))
