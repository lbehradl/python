import random
class Human:
    def __init__(self, name):
        self.name = name

class Player(Human):
    def __init__(self, name, team):
        Human.__init__(self, name)
        self.team = team
        
player_names = ["حسین", "مازیار", "اکبر", "نیما", "مهدی"
                , "فرهاد", "محمد", "خشایار", "میلاد", "مصطفی", "امین"
                , "سعید", "پویا", "پوریا", "رضا", "علی", "بهزاد"
                , "سهیل", "بهروز", "شهروز", "سامان", "محسن"]

random.shuffle(player_names)
player = []

for i in range(22):
    team_name = "Team Aval" if i<11 else "Team Dovom"
    player.append(Player(player_names[i],team_name))
    
for person in player:
    print(person.name,person.team)

