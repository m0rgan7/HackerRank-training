#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    timeCharged = float(input('Enter the time charged: ').strip())

    if timeCharged < 4:
        print(f"{2 * timeCharged:.2f} hours") #twice cuz of the training data, it goes like (5.62 / 2.81 = 2), (3.80 / 1.90 = 2)...

    else:
        print("8.00 hours")