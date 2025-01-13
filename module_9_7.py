# Домашнее задание по теме "Декораторы".
# Задание: Декораторы в Python.

def is_prime(func):
    def wrapper(*args):
        n = func(*args)
        for i in range(2, int(n / 2) + 1):
            if n % i == 0:
                print('Составное')
                return n
            print('Простое')
            return n
    return wrapper

@is_prime
def sum_three(*args):
    return sum(args)


result = sum_three(2, 3, 6)
print(result)
