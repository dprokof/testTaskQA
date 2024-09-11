import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')
USER = os.getenv('USERNAME')
REPOSITORY_NAME = os.getenv('REPOSITORY_NAME')


def test_create_public_repository():
    url = f"https://api.github.com/user/repos"
    headers = {
        "Authorization": f"token {API_KEY}"
    }
    payload = {
        "name": REPOSITORY_NAME,
        "private": False
    }
    response = requests.post(url, headers=headers, json=payload)
    return response.json()


def test_check_repository():
    url = f"https://api.github.com/repos/{USER}/{REPOSITORY_NAME}"
    response = requests.get(url)
    return response.status_code


def test_delete_repository():
    url = f"https://api.github.com/repos/{USER}/{REPOSITORY_NAME}"
    headers = {
        "Authorization": f"token {API_KEY}"
    }
    response = requests.delete(url, headers=headers)
    return response.status_code


create_repository = test_create_public_repository()
print("Repository is created", create_repository['html_url'])


check_repository = test_check_repository()
if check_repository == 200:
    print('Repository found')
else:
    print('Repository not found!')


delete_repository = test_delete_repository()
if delete_repository == 204:
    print('Repository successfully deleted')
else:
    print('Error!')