# Import pandas
import pandas as pd

# Assign spreadsheet filename to `file`
file = 'Диоды.xlsx'

# Load spreadsheet
xl = pd.ExcelFile(file)

# Print the sheet names
print(xl.sheet_names)

# Load a sheet into a DataFrame by name: df1
df1 = xl.parse('Лист1')

#получаем число строк
df1.shape[0]

#определенная строка
df1.loc[[0]]
df1.iloc[0]

#определенная ячейка
df1.iloc[0]['Наименование']

for line in range(0,df1.shape[0]):
    resulting_text = """
    Описание\n
    %s – это %s диод в %s исполнении. Имеет повторяющееся импульсное обратное напряжение URRM %d-%d В.
    Низкие статические потери. Стандартизированная конструкция. Tjmax = %d °C\n
    \n
    Где применяются\n
    Выпрямительные диоды являются одним из самым распространенных видов силовых ключей.
    Предназначены для применения в цепях постоянного и переменного тока частотой до 500 Гц в электротехнических устройствах
    общего назначения. Анодом и катодом являются плоские основания, при этом полярность определяется с помощью символа полярности, 
    нанесенного на корпус диода. Приборы имеют герметичный корпус, который изолирует функциональную часть полупроводниковый элемент 
    от воздействия внешней окружающей среды.\n
    Сферы применения:\n
    выпрямительные мосты, тяговые преобразователи, электропривод, инверторы.
    """ % (df1.iloc[line]['Наименование'], df1.iloc[line]['Тип'], df1.iloc[line]['Исполнение'], df1.iloc[line]['URRM [В min] [В min]'], df1.iloc[line]['URRM [В max] [В max]'], df1.iloc[line]['Tjmax [°С]'])
        
    print(resulting_text)