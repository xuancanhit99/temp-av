import requests

api_url = 'http://localhost:8080'


def test_healthcheck():
    response = requests.get(f'{api_url}/__health')
    assert response.status_code == 200


class TestAuthors():
    def test_get_empty_author(self):
        response = requests.get(f'{api_url}/api/authors')
        assert response.status_code == 200
        assert len(response.json()) == 0

    # def test_create_author(self):
    #
    #     body = {
    #         "name": "Leanne Graham",
    #         "username": "Bret",
    #         "email": "Sincere@april.biz",
    #         "address": "Vietnam"
    #     }
    #     response = requests.post(f'{api_url}/api/add-author', json=body)
    #     assert response.status_code == 200
    #     assert response.json().get('name') == 'Leanne Graham'
    #     assert response.json().get('username') == 'Bret'
    #     assert response.json().get('email') == 'Sincere@april.biz'
    #     assert response.json().get('address') == 'Vietnam'
    #
    # def test_get_author_by_id(self):
    #     response = requests.get(f'{api_url}/api/author/0')
    #     assert response.status_code == 200
    #     assert response.json().get('name') == 'Leanne Graham'
    #     assert response.json().get('username') == 'Bret'
    #     assert response.json().get('email') == 'Sincere@april.biz'
    #     assert response.json().get('address') == 'Vietnam'
    #
    # def test_get_not_empty_author(self):
    #     response = requests.get(f'{api_url}/api/authors')
    #     assert response.status_code == 200
    #     assert len(response.json()) == 1
