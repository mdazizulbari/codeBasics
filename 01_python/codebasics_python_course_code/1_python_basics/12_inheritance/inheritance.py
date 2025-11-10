import datetime  # Import datetime module for date/time operations

# Parent class - Base class for all types of players
class Player:
    # Constructor - initializes common attributes for all players
    def __init__(self, fname, lname, birth_year):
        self.first_name = fname        # Player's first name
        self.last_name = lname          # Player's last name
        self.birth_year = birth_year    # Year player was born
    
    # Method to calculate player's current age
    # This method is inherited by all child classes
    def get_age(self):
        now = datetime.datetime.now()      # Get current date and time
        return now.year - self.birth_year  # Current year minus birth year

# Child class - Inherits from Player, specialized for tennis
class TennisPlayer(Player):
    # Constructor - adds tennis-specific attributes
    def __init__(self, fname, lname, birth_year):
        super().__init__(fname, lname, birth_year)  # Call parent class constructor
        self.aces = []  # Empty list to store ace counts from each match
    
    # Method specific to tennis - calculates average aces per match
    def get_average_aces_per_match(self):
        return sum(self.aces) / len(self.aces)  # Total aces divided by matches played

# Child class - Inherits from Player, specialized for cricket
class CricketPlayer(Player):
    # Constructor - adds cricket-specific attributes
    def __init__(self, fname, lname, team, birth_year):
        super().__init__(fname, lname, birth_year)  # Call parent class constructor
        self.team = team       # Team the player represents (e.g., 'India')
        self.scores = []       # Empty list to store match scores
    
    # Method to add a new score to player's record
    def add_score(self, score):
        self.scores.append(score)  # Append score to the list
    
    # Method to calculate average score across all matches
    def get_average_score(self):
        return sum(self.scores) / len(self.scores)  # Total runs divided by innings

# Create a CricketPlayer object for Virat Kohli
virat = CricketPlayer('virat', 'kohli', 'india', 1988)
virat.add_score(37)   # Add first match score: 37 runs
virat.add_score(23)   # Add second match score: 23 runs
virat.add_score(85)   # Add third match score: 85 runs

# Print Virat's age: 2025 - 1988 = 37 years old
# get_age() is inherited from Player class
print("Age of viral kohli:", virat.get_age())

# Print Virat's average score: (37 + 23 + 85) / 3 = 48.33
print("Average score of viral kohli:", virat.get_average_score())

# Create a TennisPlayer object for Roger Federer
roger = TennisPlayer('roger', 'federer', 1981)

# Print Roger's age: 2025 - 1981 = 44 years old
# get_age() is inherited from Player class
print("Age of roger federer:", roger.get_age())