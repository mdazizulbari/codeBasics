import datetime

def get_average_score(player):
    return sum(player['scores'])/len(player['scores'])

def get_age(player):
    current_year = datetime.datetime.now().year
    return current_year - player["birth_year"]

# Virat Kohli

virat = {
    "firstName": "virat",
    "lastName": "kohli",
    "scores": [],
    "birth_year": 1988,
}
virat["scores"].append(80)
virat["scores"].append(100)
virat["scores"].append(0)

print(f"Virat - Average: {get_average_score(virat)}, Age: {get_age(virat)}")

# ADDED: David Warner
david = {
    "firstName": "david",
    "lastName": "warner",
    "scores": [],
    "birth_year": 1986,  # Warner born Oct 27, 1986
}
david["scores"].append(95)
david["scores"].append(120)
david["scores"].append(45)

print(f"David - Average: {get_average_score(david)}, Age: {get_age(david)}")

