name = (input('Введи свое имя: '))
transform_name = name.strip().capitalize()
age = int(input('Введи свой возраст: '))
message = ''
error = ''

index = ('лет' if (age > 14 and age <= 20) or age % 10 > 4 or age % 10 == 0 else
         'год' if age % 10 == 1 else
         'года')

if not name:
    error = 'Ошибка: введи имя!'
elif len(transform_name) < 3:
    error = 'Ошибка: в имени должно быть минимум 3 символа!'
elif len(transform_name) == 0:
    error = f'Ошибка: введи имя без пробелов!'

elif age < 0 or age == 0:
    error = 'Ошибка: введи корректный возраст!'
elif age < 14:
    error = 'Ошибка: тебе нужно подрасти до 14 лет!'
else:
    error = f'Привет, {transform_name}! Тебе {age} {index}. '

    if age == 16 or age == 17:
        message = 'Не забудь получить свой первый паспорт.'
    elif age == 25 or age == 26:
        message = 'Не забудь заменить паспорт после 25 лет.'
    elif age == 45 or age == 46:
        message = 'Не забудь заменить паспорт после 45 лет.'

print(error + message)


