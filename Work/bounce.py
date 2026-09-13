# bounce.py
#
# Exercise 1.5

# First attempt: 9-13-26 @ 3:56 PM

"""
Problem Statement:
    A rubber ball is dropped from a height of 100 meters and each time it
hits the ground, it bounces back up to 3/5 the height it fell.  Write
a program `bounce.py` that prints a table showing the height of the
first 10 bounces.
"""

drop_height = 100 # Initial height the ball was dropped from.
bounce_height = 60 # The height the ball reached on the first bounce.
number_of_bounces = 10   # The number of bounces that we want to track the height of.
current_bounce = 1 # The starting bounce to track height from

while current_bounce <= number_of_bounces:
    print(current_bounce, bounce_height)
    current_bounce += 1
    bounce_height = round(bounce_height * (3/5), 4)
