from classes import User, SocialNetwork
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

    def fetch_user_and_friends(self, username, depth=2) -> SocialNetwork:
        """
        Получает сеть взаимных друзей с указанной глубиной поиска
        Args:
            username: имя пользователя с которого начинается поиск
            depth: глубина поиска (по умолчанию 2 уровня)
        """
        network = SocialNetwork()
        processed_users = set()  # Для отслеживания уже обработанных пользователей

        def process_user(username, current_depth):
            if current_depth > depth or username in processed_users:
                return
            
            processed_users.add(username)
            
            # Получаем данные пользователя
            user_data = self.get_user_data(username)
            if not user_data or "id" not in user_data:
                return
                
            user = User(user_data["id"], user_data["login"], [])
            network.addUser(user)

            # Получаем подписки пользователя
            following = self.get_following(username)
            
            # Проверяем взаимные подписки
            for f in following:
                friend_username = f["login"]
                friend_following = self.get_following(friend_username)

                # Если есть взаимная подписка
                if any(u["login"] == username for u in friend_following):
                    friend_user = User(f["id"], f["login"], [])
                    network.addUser(friend_user)
                    network.addFriendship(user.id, friend_user.id)

                    # Рекурсивно обрабатываем друзей на следующем уровне
                    if current_depth < depth:
                        process_user(friend_username, current_depth + 1)

        # Начинаем с основного пользователя
        process_user(username, 1)
        return network
