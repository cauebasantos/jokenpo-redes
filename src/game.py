class Game():
    def __init__(self):
        self.valid_actions = ['r', 'p', 's', 'd']

    def resolve_game(self, p1_action, p2_action):
        if (p1_action == 'r' and p2_action == 's') or \
        (p1_action == 'p' and p2_action == 'r') or \
        (p1_action == 's' and p2_action == 'p'):
            return 1 # Player 1 win
        elif (p1_action == 's' and p2_action == 'r') or \
        (p1_action == 'r' and p2_action == 'p') or \
        (p1_action == 'p' and p2_action == 's'):
            return 2 # Player 1 lose
        else:
            return 3 # Its a draw

    def get_action_fullname(self, action):
        if action == 'r':
            return 'Rock(r)'
        elif action == 'p':
            return 'Paper(p)'
        else:
            return 'Scissors(s)'

    def is_valid(self, action):
        return action in self.valid_actions

    def get_valid_actions(self):
        return self.valid_actions[:-1]

    def check_disconnection(self, action):
        return True if action == 'd' else False
