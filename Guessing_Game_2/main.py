import math
from math import floor
################# My Number: 26 #######################

#print("Welcome to the Guessing Game Part 2!")
#print("Please think of a number between 1 and 100 (including).")
#print("I will now try to guess your number. Please tell me whether my guess is too low or too high!")
#print("HINT: type 'lower' or 'higher' please.")

#def main_game():
#    comp_guess = 50
#    print(comp_guess)
#   if input("\n" == 'lower')
#       comp_guess = 25
#       print(comp_guess)
#       if input("\n" == 'lower')
#           comp_guess = 12
#           print(comp_guess)
#           if input

def binary_search(A, n, T):
    L = 0
    R = n-1
    while L <= R:
        m = math.floor((L + R) / 2)
        if A[m] < T:
            L = m+1
        elif A[m] > T:
            R = m-1
        else:
            return m+1
    return "Unsuccessful"

A = list(range(1, 101))
n = len(A)
T = 67

print(binary_search(A, n, T))