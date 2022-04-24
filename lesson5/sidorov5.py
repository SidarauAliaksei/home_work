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


def main() -> str:
    """Checks the entered name and the entered age of the user for the correctness of the input.
    Displays the user's greeting with their name (capitalized),
    indication of age and advice on replacing / obtaining a passport (if the advice is relevant).

    data: name(str), age(int)- requested data keyboard input
    function: validate_name(name) - checks the name entered by the user for correctness
    validate_age(age) - checks the age entered by the user for correctness
    change_passport(age) - checks if the user needs get or replace a passport

    notes: will work until the user enters the correct name and age.
    :rtype: str
    :return: user greeting (capitalized), age, and advice on getting/replacing
    (for age values 15-16, 25-26, 45-46) or error text

    """
    message = ''

    name = input("Enter your name: ").strip().capitalize()
    valid_n = validate_name(name)
    while valid_n != "":
        print(valid_n)
        name = input("Enter you name: ").strip().capitalize()
        valid_n = validate_name(name)
    message += f"Hello, {name}! "

    age = int(input("Enter your age: "))
    valid_a = validate_age(age)
    while valid_a != "":
        print(valid_a)
        age = int(input("Enter your age: "))
        valid_a = validate_age(age)

    change_p = change_passport((age))
    message += f"You are {age} years old. {change_p}"

    return message


if __name__ == '__main__':
    print(main())
