#!/usr/bin/env python3

import random
# mega millions 1 - 70 white balls (5), 1 - 25 for mega (gold ball)
# power ball 1 - 69 white balls (5), 1 - 26 powerball (red ball)

megaNumbers = list(range(1,70))
powerNumbers = list(range(1,69))

megaWhiteBall1 = random.choice(megaNumbers)
megaNumbers.remove(megaWhiteBall1)
megaWhiteBall2 = random.choice(megaNumbers)
megaNumbers.remove(megaWhiteBall2)
megaWhiteBall3 = random.choice(megaNumbers)
megaNumbers.remove(megaWhiteBall3)
megaWhiteBall4 = random.choice(megaNumbers)
megaNumbers.remove(megaWhiteBall4)
megaWhiteBall5 = random.choice(megaNumbers)
megaGoldBall1 = random.randint(1,25)

powerWhiteBall1 = random.choice(powerNumbers)
powerNumbers.remove(powerWhiteBall1)
powerWhiteBall2 = random.choice(powerNumbers)
powerNumbers.remove(powerWhiteBall2)
powerWhiteBall3 = random.choice(powerNumbers)
powerNumbers.remove(powerWhiteBall3)
powerWhiteBall4 = random.choice(powerNumbers)
powerNumbers.remove(powerWhiteBall4)
powerWhiteBall5 = random.choice(powerNumbers)
powerBall = random.randint(1,26)

print("Here are the first five numbers for the megaball lotto", megaWhiteBall1, " ", megaWhiteBall2, " ",
      megaWhiteBall3, " ", megaWhiteBall4, " ", megaWhiteBall5)
print("The mega ball number is ", megaGoldBall1)
print("Good luck!")

print("Here are the first five numbers for the powerball lotto ", powerWhiteBall1, " ", powerWhiteBall2, " ",
      powerWhiteBall3, " ", powerWhiteBall4, " ", powerWhiteBall5)
print("The powerball number is ", powerBall)
print("Good luck!")



