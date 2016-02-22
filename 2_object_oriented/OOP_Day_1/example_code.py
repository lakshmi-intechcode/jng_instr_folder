class Athlete:

    legs = 2
    arms = 2
    is_rich = True

    def __init__(self, name, sport, team, weight):
        self.name = name
        self.sport = sport
        self.team = team
        self.weight = weight

    def appendages(self):
        return(self.arms + self.legs)


jeff = Athlete(name='jeff', sport='swimming', team='sharks', weight=500)


print(jeff.appendages())