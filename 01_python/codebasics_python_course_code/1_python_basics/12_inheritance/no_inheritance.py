import datetime  # Import datetime module for date/time operations

# Class to represent a Tennis Player
class TennisPlayer:
    # Constructor - initializes a tennis player object
    def __init__(self, fname, lname, birth_year):
        self.first_name = fname        # Player's first name
        self.last_name = lname          # Player's last name
        self.birth_year = birth_year    # Year player was born
        self.aces = []                  # Empty list to store ace counts from each match
    
    # Method to calculate player's current age
    def get_age(self):
        now = datetime.datetime.now()      # Get current date and time
        return now.year - self.birth_year  # Current year minus birth year
    
    # Method to calculate average aces per match
    def get_average_aces_per_match(self):
        return sum(self.aces) / len(self.aces)  # Total aces divided by number of matches
    
    # Method to add number of aces from a match
    def add_ace(self, num_aces):
        self.aces.append(num_aces)  # Append ace count to the list

# Class to represent a Cricket Player
class CricketPlayer:
    # Constructor - initializes a cricket player object
    def __init__(self, fname, lname, team, birth_year):
        self.first_name = fname        # Player's first name
        self.last_name = lname          # Player's last name
        self.birth_year = birth_year    # Year player was born
        self.team = team                # Team the player represents
        self.scores = []                # Empty list to store match scores
    
    # Method to calculate player's current age
    # NOTE: Code duplication - same logic as TennisPlayer.get_age()
    def get_age(self):
        now = datetime.datetime.now()      # Get current date and time
        return now.year - self.birth_year  # Current year minus birth year
    
    # Method to add a score from a match
    def add_score(self, score):
        self.scores.append(score)  # Append score to the list
    
    # Method to calculate average score across all matches
    def get_average_score(self):
        return sum(self.scores) / len(self.scores)  # Total runs divided by innings

# Create a CricketPlayer object for Virat Kohli
virat = CricketPlayer('virat', 'kohli', 'india', 1988)

# Add three match scores to Virat's record
virat.add_score(37)   # First match: 37 runs
virat.add_score(23)   # Second match: 23 runs
virat.add_score(85)   # Third match: 85 runs

# Print Virat's age: 2025 - 1988 = 37 years old
print("Age of viral kohli:", virat.get_age())

# Print Virat's average score: (37 + 23 + 85) / 3 = 48.33
print("Average score of viral kohli:", virat.get_average_score())

# Create a TennisPlayer object for Roger Federer
roger = TennisPlayer('roger', 'federer', 1981)

# Add ace counts from two matches
roger.add_ace(5)  # First match: 5 aces
roger.add_ace(7)  # Second match: 7 aces

# Print Roger's age: 2025 - 1981 = 44 years old
print("Age of roger federer:", roger.get_age())