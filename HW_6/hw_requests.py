import json
import requests


def get_a_list_of_all_authors():
    response = requests.get(url='https://fakerestapi.azurewebsites.net/api/v1/Authors').json()
    print(json.dumps(response, indent=2))


def get_author_search_by_id(id: int):
    response = requests.get(url=f'https://fakerestapi.azurewebsites.net/api/v1/Authors/{id}').json()
    print(json.dumps(response, indent=2))


def post_add_new_book_with_id_201():
    data = dict(id=201, title="string", description="string", pageCount=0, excerpt="string",
                publishDate="2022-07-13T09:38:26.890Z")
    response = requests.post(url='https://fakerestapi.azurewebsites.net/api/v1/Books/', json=data)
    print(response.status_code)
    print(response.json())


def post_add_new_user_with_id_11():
    data = {'id': 11, 'userName': 'Aliaksei', 'password': 'Password'}
    response = requests.post(url='https://fakerestapi.azurewebsites.net/api/v1/Users', json=data)
    print(response.status_code)
    print(response.json())


def refresh_data_for_book_id_10():
    changed_data = dict(id=10, title="Changed", description="Changed", pageCount=1, excerpt="Changed",
                        publishDate="2022-07-13T09:38:26.890Z")
    response = requests.put(url='https://fakerestapi.azurewebsites.net/api/v1/Books/10', json=changed_data)
    print(response.status_code)
    print(response.json())


def delete_book_with_id_4():
    response = requests.delete(url='https://fakerestapi.azurewebsites.net/api/v1/Books/4')
    print(response.status_code)


if __name__ == "__main__":
    get_a_list_of_all_authors()
    get_author_search_by_id(2)
    post_add_new_book_with_id_201()
    post_add_new_user_with_id_11()
    refresh_data_for_book_id_10()
    delete_book_with_id_4()
