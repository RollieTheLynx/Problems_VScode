'''
какие функции вызываются, с какими аргументами и что они возвращают
'''

import functools

def log_calls(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[CALL] {func.__name__} args={args} kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"[RETURN] {func.__name__} -> {result}")
        return result
    return wrapper

# Пример использования:

@log_calls
def multiply(a, b):
    return a * b

@log_calls
def summ(a, b):
    return a + b

multiply(3, 5)
summ(20, 3)