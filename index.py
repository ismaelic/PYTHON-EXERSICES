import pandas as pd
import json
import os


def createJSON(elements):
    for element in elements:
        file_extension = ".json"
        file_name = element['title'] + file_extension
    
        with open(os.path.join(file_name), 'w') as file:
            json.dump(element["content"], file)


def run():
    xl = pd.ExcelFile('formas-flexibles.xlsx', engine='openpyxl')

    # Identificar los nombres de las hojas 
    # print(xl.sheet_names)
    
    df = xl.parse('Hoja 1')
    
    columns = []

    for column in df.columns:
        if column.startswith('Unnamed'):
            break
        else:
            # print(df.loc[1:5])
            columns.append({'title': column, "content": 'contenido'})
            # for row in df.DataFrama(columns):
            #     columns.append({'title': column, "content": row})

    
    createJSON(columns)

if __name__ == '__main__':
    run()