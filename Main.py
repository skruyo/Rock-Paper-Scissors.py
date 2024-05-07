# Team 7
from dataclasses import dataclass # https://docs.python.org/3/library/dataclasses.html
from enum import Enum # https://docs.python.org/3/howto/enum.html
import random # https://docs.python.org/3/library/random.html#module-random

class Move(Enum):
   ROCK = 1
   PAPER = 2
   SCISSORS = 3

@dataclass
class Round:
   player1: Move
   player2: Move
   winner: int


def play_round(player1: Move, player2: Move) -> Round:
   # Player, AI
   winning: dict  = {
      (Move.ROCK, Move.SCISSORS): 1,
      (Move.ROCK, Move.PAPER): 0,
      (Move.ROCK, Move.ROCK): 0.5,

      (Move.PAPER, Move.ROCK): 1,
      (Move.PAPER, Move.SCISSORS): 0,
      (Move.PAPER, Move.PAPER): 0.5,

      (Move.SCISSORS, Move.PAPER): 1,
      (Move.SCISSORS, Move.ROCK): 0,
      (Move.SCISSORS, Move.SCISSORS): 0.5
   }
   game: Round = Round(player1, player2, winning[(player1, player2)])
   return game

history: list[Round] = []
def doing_same_moves(times: int) -> bool:
   global history
   consecutive_count: int = 0
   
   last_move = history[0].player1
   for round in history[::-1]: # https://www.geeksforgeeks.org/python-reversing-list/
      if round.player1 == last_move:
         consecutive_count += 1
      else:
         consecutive_count = 1
         last_move = round.player1
      if consecutive_count >= times:
         return True
   return False


def counter_move(move: Move) -> Move:
   if move == Move.ROCK:
      return Move.PAPER
   elif move == Move.PAPER:
      return Move.SCISSORS
   elif move == Move.SCISSORS:
      return Move.ROCK


def ai_play() -> Move:
   global isAnimeFan
   if len(history) == 0:
      return isAnimeFan and Move.ROCK or Move.PAPER 
   elif doing_same_moves(3):
      return counter_move(history[-1].player1)
   else:
      return random.choice(list(Move))

isAnimeFan: bool = False
def main() -> None:
   global isAnimeFan
   if input("Are you an Anime fan? y/n").find("y") != -1:
      isAnimeFan = True
   while True:
      player1: Move = Move(int(input("1. Rock\n2. Paper\n3. Scissors\n")))
      player2: Move = ai_play()
      print(f"\n\n\n\n\n\n\n\n\n\n\nPlayer: {player1.name}\nAI: {player2.name}")

      game: Round = play_round(player1, player2)
      if game.winner == 1:
         print("You win!")
      elif game.winner == 0:
         print("You lose!")
      else:
         print("Tie!")
      history.append(game)
main()
