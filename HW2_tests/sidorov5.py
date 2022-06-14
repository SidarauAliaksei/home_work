def validate_name(name: str) -> str:
    """Checks the name entered by the user for correctness.

    :param: name(str) - person's name
    :rtype: str
    :return: error text (for each condition, a different error text) or empty string

    """
    if not name:
        return "Error: empty name!"
    if len(name) < 3:
        return "Error: the name must contain at least 3 characters!"
    total = 0
    for symbol in name:
        if symbol == " ":
            total += 1
            if total > 1:
                return "Error: name can't contain more than one space!"
    else:
        return ""


def validate_age(age: int) -> str:
    """Checks the age entered by the user for correctness.

    :param: age(int) - person's age
    :rtype: str
    :return: error text (for each condition, a different error text) or empty string

    """
    if age <= 0:
        return "Error: enter the correct age!"
    if age < 14:
        return "Error: you need to grow up to 14 years old!"
    else:
        return ""


def change_passport(age: int) -> str:
    """Checks if the user needs get or replace a passport.

    :param: age(int) - person's age
    :rtype: str
    :return: advice for getting/replacing a passport or an empty string

    """
    if 16 <= age <= 17:
        return "Don't forget to get your first passport."
    if 25 <= age <= 26:
        return "Don't forget to replace your passport after 25 years."
    if 45 <= age <= 46:
        return "Don't forget to replace your passport after 45 years."
    return ""

def clean(name:str) -> str:
    """Removes space in a string.

    :param: name: name(str) -> person's name
    :rtype: str
    :return: removes space at the beginning and end of a string

    """
    transform_name = name.strip()
    return transform_name

def main(name, age):
    if validate_name(name) == '' and validate_age(age) == '':
        return f'Hello, {name}. You are {age} years old. {change_passport(age)}'
    else:
        return f'{validate_name(name)}  {validate_age(age)}'

