#!/usr/local/bin/python

import argparse
import textwrap

# handle options...

parser = argparse.ArgumentParser()

parser.add_argument('-v', action='store_true', default=False,
                    help='make more, yer know, wossname')
                    
parser.add_argument('-p', action='store', dest='planet', default='World',
                    help='Alternative location')
                    
args = parser.parse_args()

# print the message...

print("Hello,", args.planet + '!')

if args.v:
    print(textwrap.dedent(
        """
            By the way, did you know that:               
            The origin of "Hello, World!" is said to be "The C Programming Language" 
            by Brian Kernighan and Dennis Ritchie.
            
            (Wikipedia [citation needed])
        """
    ))
