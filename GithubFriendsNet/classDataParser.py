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

    def fetch_extended_network(self, username) -> SocialNetwork:
        network = SocialNetwork()

        user_data = self.get_user_data(username)
        main_user = User(user_data["id"], user_data["login"], [])
        network.addUser(main_user)

        # Перший рівень — друзі користувача
        level1_friends = self.get_following(username)

        for f in level1_friends:
            friend = User(f["id"], f["login"], [])
            network.addUser(friend)
            network.addFriendship(main_user.id, friend.id)

            # Другий рівень — друзі друга
            friend_following = self.get_following(friend.username)

            for ff in friend_following:
                ff_user = User(ff["id"], ff["login"], [])
                network.addUser(ff_user)
                network.addFriendship(friend.id, ff_user.id)

        return network
