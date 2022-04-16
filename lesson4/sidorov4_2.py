name = (input('Введи свое имя: '))
transform_name = name.strip().capitalize()
age = int(input('Введи свой возраст: '))
name_message = ''
name_error = ''
age_message = ''
age_error = ''
passport_message = ''

index = ('лет' if (age > 14 and age <= 20) or age % 10 > 4 or age % 10 == 0 else
         'год' if age % 10 == 1 else
         'года')

if not name:
    name_error = 'Ошибка: введи имя!'
elif len(transform_name) < 3:
    name_error = 'Ошибка: в имени должно быть минимум 3 символа!'
elif len(transform_name) == 0:
    name_error = f'Ошибка: введи имя без пробелов!'
else:
    name_message =f'Привет {transform_name}! '

if age < 0 or age == 0:
    age_error = 'Ошибка: введи корректный возраст!'
elif age < 14:
    age_error = 'Ошибка: тебе нужно подрасти до 14 лет!'
if name_message != '':
    name_message += f'Тебе {age} {index}. '

if age == 16 or age == 17:
    passport_message = 'Не забудь получить свой первый паспорт.'
elif age == 25 or age == 26:
    passport_message = 'Не забудь заменить паспорт после 25 лет.'
elif age == 45 or age == 46:
    passport_message = 'Не забудь заменить паспорт после 45 лет.'
if name_message != '':
    name_message += passport_message

print(name_error, age_error, name_message)
