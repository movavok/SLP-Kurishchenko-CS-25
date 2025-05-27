class User:
    def __init__ (self, id, username, friendsList):
        self.id = id
        self.username = username
        self.friendsList = friendsList
    def __str__(self):
        return f"User(id={self.id}, username='{self.username}', friendsList={self.friendsList})"
    
    def addFriend(self, friendId):
        if friendId not in self.friendsList: self.friendsList.append(friendId)
    def removeFriend(self, friendId): 
        if friendId in self.friendsList: self.friendsList.discard(friendId)
    def getFriends(self): return self.friendsList