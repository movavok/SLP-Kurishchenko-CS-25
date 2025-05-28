class SocialNetwork:
    def __init__(self):
        self.users = {}
        self.friendships = {}

    def addUser(self, user):
        if user.id not in self.users:
            self.users[user.id] = user
            self.friendships[user.id] = set()

    def deleteUser(self, userId):
        if userId in self.users:
            del self.users[userId]
            del self.friendships[userId]
            for friends in self.friendships.values(): friends.discard(userId)

    def addFriendship(self, userId1, userId2):
        if userId1 in self.users and userId2 in self.users:
            self.friendships[userId1].add(userId2)
            self.friendships[userId2].add(userId1)

    def findUsersFriendship(self, userId):
        if userId in self.friendships: return self.friendships[userId]
        return None
    
    def centralityOfUsers(self, userId):
        if userId not in self.users: return 0
        friends = self.friendships[userId]
        if not friends: return 0
        return len(friends) / (len(self.users) - 1)