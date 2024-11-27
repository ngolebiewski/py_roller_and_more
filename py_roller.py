import random
import argparse

"""
PURPOSE: Learn the basics of the argparse library by example.

I take some args.
Lets say I think dice are cool, and need to play with D&D
positional:
num sides: sides
num rolls: rolls
optional keyword arg:
talk old-timey
"""

parser = argparse.ArgumentParser()
parser.add_argument("sides", help="How many sides does the die have, i.e. 6, 20...", type=int)
parser.add_argument("rolls", help="Enter the number of rolls to make", type=int)
parser.add_argument("--old_timey", help="Choose this flag if you want the language to be old timey", action="store_true")
args = parser.parse_args()

def roll_dice(sides, rolls):
    results = list()
    for _ in range(rolls):
        results.append(random.randint(1, sides))
    return results

def talk_dice(results):
    """results is a list of ints"""
    if args.old_timey:
        return f"Thou rolled thy {args.sides} sided die {args.rolls} times and received:\n{results}"
    else:
        return f"You rolled a {args.sides} sided die {args.rolls} times and got:\n{results}"

def main():
    results = roll_dice(args.sides, args.rolls)
    print(talk_dice(results))

if __name__ == "__main__":
    main()
