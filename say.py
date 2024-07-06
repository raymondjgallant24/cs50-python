import sys
from sayings.py import hello

if len(sys.argv) == 2:
    hello(sys.argv[1])

