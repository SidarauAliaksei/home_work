from time import time, sleep

f = lambda a: print('Четное') if a % 2 == 0 else print('Нечетное')

print()


lst = [2, 3, 4, 5, 2, 1]
print(list(map(lambda x: str(x), lst)))

print()

words = ('казак', 'отец', 'мадам', 'машина', 'кок')
palindromes = (list(filter(lambda word: word == word[::-1], words)))
print(palindromes)

print()

def decorator(func):
    def wrapper(*args, **kwargs):
        print('Результат выполнения функции: ')
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        total_time = round(end_time - start_time, 5)
        print(f'Функция {func.__name__} выполнялась {total_time} секунд.')
        return result

    return wrapper


@decorator
def pow_number(number, degree):
    sleep(0.5)
    return f'Число {number} в степени {degree} = {number ** degree}.'


print(pow_number(3, 2))

print()


@decorator
def is_palindrome(word: str) -> str:
    sleep(0.5)
    i = 0
    j = len(word) - 1
    while i < j:
        if word[i] != word[j]:
            return 'Слово палиндромом не является.'
        i += 1
        j -= 1
    return 'Слово явлется палиндромом.'


print(is_palindrome('вода'))

print()


def check_string():
    x = input('Введите число: ')
    if (x.isdigit()):
        return f'Вы ввели положительное целое число: {int(x)}.'
    if x[0] == '-' and x[1:].isdigit():
        return f'Вы ввели отрицательное  целое число: {int(x)}.'
    if x.replace('.', '').isdigit():
        return f'Вы ввели положительное дробное число: {float(x)}.'
    if x[0] == '-' and x[1:].replace('.', '').isdigit():
        return f'Вы ввели отрицательное дробное число: {float(x)}.'

    else:
        return f'Вы ввели некорректное число: {x}'


print(check_string())
