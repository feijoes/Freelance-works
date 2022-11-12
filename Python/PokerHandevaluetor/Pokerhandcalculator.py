#!/usr/bin/env python3
import sys
import time
from datetime import datetime
from typing import List, Tuple
from collections import defaultdict
CRLF = "\n"
SP = " "
suits = ["C", "D", "H", "S"]
values = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]

# ESCRIBA SU CODIGO AQUI
card_order_dict = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "T":10,"J":11, "Q":12, "K":13, "A":14}
# NO MODIFIQUE EL RESTO


def is_flush(hand: List[str]) -> Tuple[bool, List[int]]:
    suits = [h[1] for h in hand]
    
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1
    if len(set(suits)) == 1:
      return (True,[sorted(value_counts.values())])
    else:
      return (False,[sorted(value_counts.values())])
  

def is_straight(hand: List[str]) -> Tuple[bool, List[int]]:
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v] += 1
    rank_values = [card_order_dict[i] for i in values]
    value_range = max(rank_values) - min(rank_values)
    if len(set(value_counts.values())) == 1 and (value_range==4):
        return (True,[sorted(value_counts.values())])
    else:
        if set(values) == set(["A", "2", "3", "4", "5"]):
            return (True,[sorted(value_counts.values())])
        return (False,[sorted(value_counts.values())])

def is_straight_flush(hand: List[str]) -> Tuple[bool, List[int]]:
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1
    if is_flush(hand)[0] and is_straight(hand)[0]:
        return (True,[sorted(value_counts.values())])
    else:
        return (False,[sorted(value_counts.values())])

def is_four_of_a_kind(hand: List[str]) -> Tuple[bool, List[int]]:
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1
    if sorted(value_counts.values()) == [1,4]:
        return (True,[sorted(value_counts.values())])
    return (False,[sorted(value_counts.values())])

def is_full_house(hand: List[str]) -> Tuple[bool, List[int]]:
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1
    if sorted(value_counts.values()) == [2,3]:
        return (True,[sorted(value_counts.values())])
    return (False, [sorted(value_counts.values())])

def is_three_of_a_kind(hand: List[str]) -> Tuple[bool, List[int]]:
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1
    if set(value_counts.values()) == set([3,1]):
        return (True,[sorted(value_counts.values())])
    else:
        return (False,[sorted(value_counts.values())])
    
def is_two_pairs(hand: List[str]) -> Tuple[bool, List[int]]:
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1
    if sorted(value_counts.values())==[1,2,2]:
        return (True,[sorted(value_counts.values())])
    else:
        return (False,[sorted(value_counts.values())])

def is_pair(hand: List[str]) -> Tuple[bool, List[int]]:
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1
    if 2 in value_counts.values():
        return (True,[sorted(value_counts.values())])
    else:
        return (False,[sorted(value_counts.values())])

def is_high_card(hand: List[str]) -> Tuple[bool, List[int]]:
    values = [i[0] for i in hand]
    rank_values = [card_order_dict[i] for i in values]
    return True ,rank_values

def find_hand(hand: List[str]) -> Tuple[bool, List[int]]:
    rank_values = is_high_card(hand)[1]
    if is_straight_flush(hand)[0]:
        return True, [9] + rank_values
    if is_four_of_a_kind(hand)[0]:
        return True, [6] + rank_values
    if is_full_house(hand)[0]:
        return True, [7] + rank_values
    if is_flush(hand)[0]:
        return True, [6] + rank_values
    if is_straight(hand)[0]:
        return True, [5] + rank_values
    if is_three_of_a_kind(hand)[0]:
        return True, [4] + rank_values
    if is_two_pairs(hand)[0]:
        return True,[3] + rank_values
    if is_pair(hand)[0]:
        return True ,[1] + rank_values
    return False, rank_values
    
def parse_hands(line: str) -> Tuple[List[str], List[str]]:
    black = sorted(line[:-1].split(" ")[:5], key=lambda card: values.index(card[0]))
    white = sorted(line[:].split(" ")[5:], key=lambda card: values.index(card[0]))

    return black, white



def compare_hands(line: str) -> int:
    # possible values are: 0 == tie, 1 == black wins, 2 == white wins
    wins = 0 # assume a tie
    black, white = parse_hands(line)
    black_hand, black_scores = find_hand(black)
    white_hand, white_scores = find_hand(white)
    if (black_hand > white_hand):
        wins = 1
    elif (black_hand < white_hand):
        wins = 2
    else:
        # the hand is a tie, compare the scores to untie
        for i in range(len(black_scores)):
            if (black_scores[i] > white_scores[i]):
                wins = 1
                break
            elif (black_scores[i] < white_scores[i]):
                wins = 2
                break
    return wins

def evaluate_hands(filename: str, outfilename: str):
    file = open(filename, "r")
    fout = open(outfilename, "w")
    for line in file.readlines():
        wins = compare_hands(line)
        fout.write("El negro gana.\n" if wins == 1 else "El blanco gana.\n" if wins == 2 else "Empate.\n")

def validate_games(solution: str, correct: str, n: int):
    with open(solution, "r") as sol, open(correct, "r") as corr:
        sol_lines = sol.readlines()
        corr_lines = corr.readlines()
        cnt = 0
        for i in range(len(sol_lines)):
            if (sol_lines[i] == corr_lines[i]):
                cnt += 1
        print("Performance = ", cnt * 100 / n)

def main(problem_path: str, solution_path: str, correct_path: str):
    now = datetime.now()
    dt_string = now.strftime("%H:%M:%S")
    print("Start time", dt_string)
    startTime = time.time()

    # run evaluation and validation
    evaluate_hands(problem_path, solution_path)
    validate_games(solution_path, correct_path, 1000)

    executionTime = (time.time() - startTime)
    now = datetime.now()
    dt_string = now.strftime("%H:%M:%S")
    print("End time", dt_string)
    print('Execution time in seconds: ' + str(executionTime))

if __name__ == "__main__":
    # this program is called with the following three paths
    # problem file, solution file, and correct answers file
    #
    # How to call this program from the command prompt:
    #
    #      python proyecto-1-nombre-apellido.py problema.txt respuesta.txt solucion.txt 
    #
    main(sys.argv[1], sys.argv[2], sys.argv[3])
    