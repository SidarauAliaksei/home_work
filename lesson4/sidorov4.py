name = (input('Введи свое имя: '))
transform_name = name.strip().capitalize()
age = int(input('Введи свой возраст: '))

index = ('лет' if (age > 14 and age <= 20) or age % 10 > 4 or age % 10 == 0 else
         'год' if age % 10 == 1 else
         'года')

name_message = ('Ошибка: введи имя!' if not name else
                'Ошибка: в имени должно быть минимум 3 символа!' if len(transform_name) < 3 else
                'Ошибка: имя не может состоять из пробелов!' if len(transform_name) == 0 else
                f'Привет, {transform_name}!')

age_message = ('Ошибка: введи корректный возраст!' if age < 0 or age == 0 else
               'Ошибка: тебе нужно подрасти до 14 лет!' if age < 14 else
               f'Тебе {age} {index}.' if age >= 14 else
               '')

passport_message = ('Не забудь получить свой первый паспорт.' if age == 16 or age == 17 else
                    'Не забудь заменить паспорт после 25 лет.' if age == 25 or age == 26 else
                    'Не забудь заменить паспорт после 45 лет.' if age == 45 or age == 46 else
                    '')
print(f'\n{name_message}\n{age_message}\n{passport_message}')
