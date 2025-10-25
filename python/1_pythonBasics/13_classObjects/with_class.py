import datetime


class CricketPlayer:
    team_size = 11

    def __init__(self, first_name, last_name, birth_year, team):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        self.team = team
        self.scores = []

    def add_score(self, score):
        self.scores.append(score)

    def get_average_score(self):
        return sum(self.scores) / len(self.scores)

    def get_age(self):
        current_year = datetime.datetime.now().year
        return current_year - self.birth_year

    def __str__(self):
        return (
            f"{self.first_name} {self.last_name}, the cricket player form {self.team}"
        )

    def __lt__(self, other):  # lt = less than operator
        self_avg_score = self.get_average_score()
        other_avg_score = other.get_average_score()
        return self_avg_score < other_avg_score

    def __eq__(self, other):
        self_age = self.get_age()
        other_age = other.get_age()
        return self_age == other_age


# Virat Kohli
virat = CricketPlayer("virat", "kohli", 1988, "India")
virat.add_score(37)
virat.add_score(100)
virat.add_score(27)

print(virat.first_name)
print(virat.last_name)
print(virat.birth_year)
print(virat.scores)
print(virat.get_average_score())
print(f"Age of Virat {virat.get_age()}")
print(virat)


# ADDED: David Warner
david = CricketPlayer("david", "warner", 1986, "Australia")
david.add_score(95)
david.add_score(120)
david.add_score(45)

print(david.first_name)
print(david.last_name)
print(david.birth_year)
print(david.scores)
print(david.get_average_score())
print(f"Age of David {david.get_age()}")  # ADDED: Missing age print for David
print(david)  # ADDED: Missing __str__ call for David

print(virat.get_average_score())
print(david.get_average_score())
print(david < virat)
print(david == virat)
