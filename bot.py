import PRAW

shitlords = []
file = open("data", "w")
for line in file:
    s = line.split()
    shitlords.add(Shitlord(s[0], int(s[1]), int(s[2]))
    
print shitlords

class Shitlord:
    def __init__(n, p = 100, o = 0):
        name = n
        privilege = p
        oppressionPoints = 0
        
    def __str__():
        print "/u/" + name + ", Privilege: " + privilege + ", Oppression: " + oppression
    
    def setPrivilege(p):
        privilege = p
        
    def giveOppression
