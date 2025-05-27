from classUser import User
from classSocialNetwork import SocialNetwork
import requests

class DataParser:
    def __init__(self, token):
        self.token = token
        self.headers = {"Authorization": f"token {self.token}"}

    def get_user_data(self, username):
        url = f"https://api.github.com/users/{username}"
        response = requests.get(url, headers=self.headers)
        return response.json()

    def get_following(self, username):
        url = f"https://api.github.com/users/{username}/following"
        response = requests.get(url, headers=self.headers)
        return response.json()

    def fetch_user_and_friends(self, username) -> SocialNetwork:
        network = SocialNetwork()

        user_data = self.get_user_data(username)
        user = User(user_data["id"], user_data["login"], [])
        network.addUser(user)

        friends = self.get_following(user_data["login"])
        for f in friends:
            friend_user = User(f["id"], f["login"], [])
            network.addUser(friend_user)

            # встановлюємо дружбу
            network.addFriendship(user.id, friend_user.id)

        return network