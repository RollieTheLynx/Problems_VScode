def findAverage(*args):
    sum = 0
    for n in args:
        sum += n
    return sum / len(args)

print(findAverage(5, 10))
print(findAverage(5, 10, 200, -600))
print(findAverage(0))
print(findAverage(5, 10, 5, 10, 5, 10, 5, 10))


def readData(**kwargs):
    print(kwargs.items())
    for key, value in kwargs.items():
        print(f'{key} equals {value}')

readData(temperature=40.8, moisture=80)
