#!/usr/bin/env python3

"""Simulate the Monty Hall problem.

"""

import argparse, random

def simulate(num_doors, switch):
    """(int, bool): bool

    Carry out the game for one contestant.  If 'switch' is True,
    the contestant will switch their chosen door when offered the chance.
    """

    # Doors are numbered from 0 up to num_doors-1 (inclusive).

    # Randomly choose the door 
    winning_door = random.randint(0, num_doors-1)
    
    # The contestant picks a random door, too.
    choice = random.randint(0, num_doors-1)

    # Pick a list of all but two doors to open.
    available_doors = list(range(num_doors))
    while len(available_doors) > 2:
        door_to_remove = random.choice(available_doors)
        if door_to_remove in (winning_door, choice):
            continue
        available_doors.remove(door_to_remove)

    # Does the contestant want to switch their choice?
    if switch:
        available_doors.remove(choice)
        
        assert len(available_doors) == 1
        choice = available_doors.pop()

    # Did the contestant win?
    return (choice == winning_door)


def main():
    # Get command-line arguments
    parser = argparse.ArgumentParser(
        description='simulate the Monty Hall problem')
    parser.add_argument('--doors', default=3, type=int, metavar='int',
                        help='number of doors offered to the contestant')
    parser.add_argument('--trials', default=10000, type=int, metavar='int',
                        help='number of trials to perform')
    args = parser.parse_args()
    
    print('Simulating {0} contestants...'.format(args.trials))

    # Carry out the trials
    winning_non_switchers = 0
    winning_switchers = 0
    for i in range(args.trials):
        # First, do a trial where the contestant never switches.
        won = simulate(args.doors, switch=False)
        if won:
            winning_non_switchers += 1
            
        # Next, try one where the contestant switches.
        won = simulate(args.doors, switch=True)
        if won:
            winning_switchers += 1
        
    print('    Switching won {0:5} times out of {1} ({2}%)'.format(
            winning_switchers, args.trials,
            (winning_switchers / args.trials * 100 ) ))
    print('Not switching won {0:5} times out of {1} ({2}%)'.format(
            winning_non_switchers, args.trials,
            (winning_non_switchers / args.trials * 100 ) ))
            
    
if __name__ == '__main__':
    main()
