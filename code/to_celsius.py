#!/usr/bin/env python3

import sys

def convert_f2c(S):
    """(str): float

    Converts a Fahrenheit temperature represented as a string
    to a Celsius temperature.
    """
    fahrenheit = float(S)
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

def main():
    # If no arguments were given, print a helpful message
    if len(sys.argv) == 1:
        print('Usage: {} temp1 temp2 ...'.format(sys.argv[0]))
        sys.exit(0)

    # Loop over the arguments
    for arg in sys.argv[1:]:
        try:
            celsius = convert_f2c(arg)
        except ValueError:
            print("{!r} is not a numeric value".format(arg),
                  file=sys.stderr)
        else:
            print('{}\N{DEGREE SIGN}F = {:g}\N{DEGREE SIGN}C'.format(
                    arg, round(celsius, 0)))

if __name__ == '__main__':
    main()
