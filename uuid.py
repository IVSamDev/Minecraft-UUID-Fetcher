import requests
import sys

def get_uuid(username):
    url = f"https://api.mojang.com/users/profiles/minecraft/{username}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        uuid = data.get("id")
        print(f"UUID for nickname {username}: {uuid}")
        return uuid
    else:
        print(f"The player with the nickname {username} not found.")
        return None

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python uuid.py <nickname>")
    else:
        username = sys.argv[1]
        get_uuid(username)
