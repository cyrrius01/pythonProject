#!/usr/bin/env python3

import random
# mega millions 1 - 70 white balls (5), 1 - 25 for mega (gold ball)
# power ball 1 - 69 white balls (5), 1 - 26 powerball (red ball)

megaNumbers = list(range(1,70))
powerNumbers = list(range(1,69))
x = 0
while x < 5:
    megaWhiteBall: int = random.choice(megaNumbers)
    x += 1
    print("Ball ",x," is ",megaWhiteBall)
    megaNumbers.remove(megaWhiteBall)
megaGoldBall: int = random.randint(1,25)
print("Megaball is: ",megaGoldBall)
print("")
x = 0

while x < 5:
    powerWhiteBall: int = random.choice(powerNumbers)
    x += 1
    print("Ball ",x," is ",powerWhiteBall)
    powerNumbers.remove(powerWhiteBall)
powerBall: int = random.randint(1,26)
print("Powerball is: ",powerBall)


