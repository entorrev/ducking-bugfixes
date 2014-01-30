import praw

class User:
    def __init__(self, n, p = 100, o = 0):
        self.name = n
        self.privilege = p
        self.points = o
        return

    def __repr__(self):
         return self.name + ", Privilege: " + str(self.privilege) + ", Points: " + str(self.points)
    
records = open("data", "r+")
users = {}

for line in records:
    s = line.split()
    users[s[0]] = User(s[0], int(s[1]), int(s[2]))

print users

