import datetime  # Import datetime module to work with dates and time

# Define a custom class to represent a cricket player
class CricketPlayer:
    # Class variable - shared by all instances of CricketPlayer
    team_size = 11  # Standard cricket team has 11 players
    
    # Constructor - initializes a new player object
    def __init__(self, fname, lname, birth_year, team):
        self.first_name = fname        # Player's first name
        self.last_name = lname          # Player's last name
        self.birth_year = birth_year    # Year the player was born
        self.team = team                # Team the player belongs to
        self.scores = []                # Empty list to store match scores
    
    # Method to add a score to the player's score list
    def add_score(self, score):
        self.scores.append(score)  # Append new score to the list
    
    # Method to calculate average score across all matches
    def get_average_score(self):
        return sum(self.scores) / len(self.scores)  # Sum of scores divided by number of scores
    
    # Method to calculate player's current age
    def get_age(self):
        now = datetime.datetime.now()      # Get current date and time
        return now.year - self.birth_year  # Current year minus birth year
    
    # Special method - defines how object is represented as string
    def __str__(self):
        return f"{self.first_name} {self.last_name}, the cricket player from {self.team}"
    
    # Special method - defines "less than" comparison between two players
    # Compares based on average score
    def __lt__(self, other):
        self_avg_score = self.get_average_score()    # Get this player's average
        other_avg_score = other.get_average_score()  # Get other player's average
        return self_avg_score < other_avg_score      # Return True if self has lower average
    
    # Special method - defines "equal to" comparison between two players
    # Compares based on age, not performance
    def __eq__(self, other):
        self_age = self.get_age()        # Get this player's age
        other_age = other.get_age()      # Get other player's age
        return self_age == other_age     # Return True if both are same age

# Create a CricketPlayer object for Virat Kohli
virat = CricketPlayer('virat', 'kohli', 1988, 'India')
virat.add_score(37)   # Add first match score
virat.add_score(100)  # Add second match score
virat.add_score(23)   # Add third match score

# Create a CricketPlayer object for David Warner
david = CricketPlayer('david', 'warner', 1988, 'australia')
david.add_score(37)   # Add first match score
david.add_score(23)   # Add second match score
david.add_score(85)   # Add third match score

# Print Virat's average score: (37 + 100 + 23) / 3 = 53.33
print("Virat avg score: ", virat.get_average_score())

# Print David's average score: (37 + 23 + 85) / 3 = 48.33
print("David avg score: ", david.get_average_score())

# Compare players using __lt__ method - checks if Virat's avg < David's avg
# Result will be False because 53.33 > 48.33
print("Is virat less than david: ", virat < david)