import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 != 0:
        print("Tubatu")
    elif n in range(2, 29):
        print("bbini")
    elif n > 29:
        print("you're tooooo old")