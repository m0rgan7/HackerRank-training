#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    timeCharged = float(input().strip())

    if timeCharged < 4:
        print(f"{2 * timeCharged:.2f}")
    else:
        print("8.00")