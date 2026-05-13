import requests

database= {
    1: "Djibril",
    2: "Moussa",
    3: "Jossonjo"
}

def get_user_from_db(user_id: int):
    return database.get(user_id)


def get_users():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    if response.status_code == 200:
        return response.json()
    
    raise requests.HTTPError


