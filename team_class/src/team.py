class Team:
    
    # Declaring data-types
    team_name = ""
    team_players = []
    player_coach = ""

    # Initialising Class object
    def __init__(self, team_name, team_players, player_coach):
        self.name = team_name
        self.players = team_players
        self.coach = player_coach
        # Since this isn't in the initial class description, it can be added here and only shows up if mentioned in the function itself.
        self.points = 0

    # Function to add player
    def add_player(self, new_player):
        self.players.append(new_player)

    # Function to see if player exists
    def has_player(self, player_name):
        return player_name in self.players

    # Incorrect attempt (it returned True and not the player name. The test asked was the name True. Lesson, always read the tests!):
    #     for player_name in self.players:
    #         if player_name == self.players:
    #             return True
    #     else:
    #         return False

    # Function to add points if team win
    def play_game(self, bool):
        if bool == True:
            self.points += 3
            
