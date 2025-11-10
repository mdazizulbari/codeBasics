import datetime  # Import datetime module to work with dates and time

# Function to calculate a player's age
# Takes a dictionary (player) as input
def get_age(player):
    now = datetime.datetime.now()              # Get current date and time
    return now.year - player['birth_year']     # Subtract birth year from current year

# Function to calculate a player's average score
# Takes a dictionary (player) as input
def get_average_score(player):
    return sum(player['scores']) / len(player['scores'])  # Sum all scores, divide by count

# Create a dictionary to represent Virat Kohli
# Dictionary stores player data as key-value pairs
virat = {
   'first_name': 'virat',     # Key: 'first_name', Value: 'virat'
   'last_name': 'kohli',      # Key: 'last_name', Value: 'kohli'
   'scores': [],              # Key: 'scores', Value: empty list (will store match scores)
   'birth_year': 1988         # Key: 'birth_year', Value: 1988
}

# Add scores to Virat's scores list
virat['scores'].append(80)    # Access 'scores' list and append 80
virat['scores'].append(100)   # Append 100 to the list
virat['scores'].append(0)     # Append 0 to the list (duck/out for 0 runs)

# Print Virat's age: 2025 - 1988 = 37 years old
print(get_age(virat))

# Print Virat's average score: (80 + 100 + 0) / 3 = 60.0
print(get_average_score(virat))

# Create a dictionary to represent David Warner
david = {
   'first_name': 'david',     # First name
   'last_name': 'warner',     # Last name
   'scores': [],              # Empty list for scores
   'birth_year': 1986         # Born in 1986
}

# Add scores to David's scores list
david['scores'].append(35)    # First match: 35 runs
david['scores'].append(120)   # Second match: 120 runs (century)
david['scores'].append(12)    # Third match: 12 runs

# Print David's age: 2025 - 1986 = 39 years old
print(get_age(david))

# Print David's average score: (35 + 120 + 12) / 3 = 55.67
print(get_average_score(david))