'''
Посмотреть все системные переменные в PowershelL:
    dir env:

Посмотреть онкретную переменную:
    $env:Path

Задать переменную:
    $env:FRUIT = 'Pineapple'
The above method we have seen is to set the environment variable temporarily,
once you close the PowerShell console the value gets destroyed.

Because an environment variable can't be an empty string,
setting one to $null or an empty string removes it.
For example:
$Env:Fruit = ''

Задать постоянную переменную:
    [Environment]::SetEnvironmentVariable('Fruit', 'Pineapple', 'Machine')
(must run Powershell as admin)
не сохраняется?

'''

import os
import sys

for key, value in os.environ.items():
    print(f'{key}: {value}')


print(f"USERNAME: {os.environ.get('USERNAME', '')}")
print(f"NUMBER_OF_PROCESSORS: {os.environ.get('NUMBER_OF_PROCESSORS', '')}")
print(f"FRUIT: {os.environ.get('FRUIT', '')}")


# Set environment variables
os.environ['API_USER'] = 'username'
os.environ['API_PASSWORD'] = 'secret'

# Get environment variables
USER = os.getenv('API_USER')
PASSWORD = os.environ.get('API_PASSWORD')
print(USER)
print(PASSWORD)

# Getting non-existent keys
FOO = os.getenv('FOO') # None
BAR = os.environ.get('BAR') # None
# BAZ = os.environ['BAZ'] # KeyError: key does not exist.


# Command-Line Arguments
print(sys.argv)


# Exit Status

# Благополучно исполняем программу:
# python "C:\Users\Mike\Documents\Python_Scripts\Problems_VScode\Small excersises\system variables.py"

# $LASTEXITCODE
# 0 - успех
# иначе неуспех



breakit = False
if breakit == True:
    sys.exit(77)