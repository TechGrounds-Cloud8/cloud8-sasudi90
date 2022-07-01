# The player_move plays against a comp_move opponent typing either a letter (rps) or an entire word (rock paper scissors) to play their move.
# Create a function that checks whether the move is valid or not.
# Create another function to create a comp_move move.
# Create another function to check who wins the round.
# Finally, create a function that keeps track of the score.
# The game should be played in a predetermined number of rounds.

import random

def get_comp_move():
    #assign a value to computer move by using random.randint and give a range
    return random.randint(0, 2)

def print_move(move, name =""):
    #print player (name or comp) and print move by putting indexnummer at moves[]
    print(name, "whips out " + moves[move])

def validate(player_move):
    #check if player_move is in list moves
    if player_move in moves:
        return True
    else:
        return False

def convert(player_move):
    #get index of player_move
    if player_move in moves:
        return moves.index(player_move)

def who_wins(player_move, comp_move):
    if player_move == comp_move:
        return "Draw"
    elif player_move - comp_move == -1 or player_move - comp_move == 2:
        return "Lose"
    else:
        return "Win"

def scoreboard(player_score, comp_score):
    if who_wins(player_move, comp_move) == "Win":
        player_score += 1
    elif who_wins(player_move, comp_move) == "Lose":
        comp_score += 1
    return player_score, comp_score

round = 0
moves = ["rock", "paper", "scissors"]
comp_move = get_comp_move()
player_score = 0
comp_score = 0

player_name = input('Please enter your name: ')
print('THINK FAST: (rock, paper, scissors)')

while round < 3 and player_score < 2 and comp_score < 2:
    print("Round", round + 1)
    player_move = input('So.... pick your move: ')
    
    if validate(player_move):
        player_move = convert(player_move)
        
        print_move(player_move, player_name)
        print_move(comp_move, 'Computer')

        result = who_wins(player_move, comp_move)
        print('Result: ' + result)
        
        player_score, comp_score = scoreboard(player_score, comp_score)
        print("Scoreboard: ", player_name, "-", player_score, ": Computer -", comp_score) 

        round += 1
        
    else:
        print('Did u faceroll? rock, paper or scissors!')

