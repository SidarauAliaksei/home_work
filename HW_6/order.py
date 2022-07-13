import yaml
import json
import datetime


with open('order.yaml') as f:
    templates = yaml.safe_load(f)
    print(templates)
    print(f"Invoice number: {templates['invoice']}")
    print(f"Shipping address: {templates['ship-to']['address']['lines']}")
    print(f"Product 1: {templates['product'][0]}")
    print(f"Product 2: {templates['product'][1]}")


def default_converter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()


def create_json():
    with open('order.yaml', 'r') as file:
        configuration = yaml.safe_load(file)

    with open('order.json', 'w') as json_file:
        print(json.dump(configuration, json_file, default=default_converter, indent=2))


def create_yaml():
    register_yaml = """
    first_name: 'Aliaksei'
    last_name : 'Sidarau'
    email     : '111@gmail.com'
    country   : 'Belarus'

    """
    names = yaml.safe_load(register_yaml)
    with open('register.yaml', 'w') as file:
        yaml.dump(names, file)


if __name__ == "__main__":
    create_json()
    create_yaml()
