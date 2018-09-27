# File:        Squarelotrons.py
# Programmer:  Shuting Sun
# Time:        Oct 2, 2016
# Description: CIT 590, Assignment 5.
#              A Squarelotron consist basically of a matrix of numbers.
#              This matrix can be decomposed as square rings which can rotate independently in 4 different ways:
#              Upside-Down (↕), Left-Right (↔), reflected through the Inverse Diagonal ( / ), and reflected through the Main Diagonal ( \ ) . 

from math import *
from copy import deepcopy

def make_squarelotron(flat_list):
    """Given a "flat" list of 25 numbers, make and return a squarelotron."""
    length = int(sqrt(len(flat_list))) # Assume the lenght of flat_list is a square number
    res = [[] for x in range(length)] # Initialize a blank two dimentional list
    for j in range(len(flat_list)):
        res[j//length].append(flat_list[j]) 
    return res

def make_list(squarelotron):
    """sum adds a sequence together using the + operator.
       + on 2 lists concatenates them together.
       This is a trick for two-dimensional lists."""
    return sum(squarelotron, [])

def upside_down_flip(squarelotron, ring):
    """Performs the Upside-Down Flip of the squarelotron."""
    u_d_s = deepcopy(squarelotron) # Use deepcopy, the original squarelotron isn't be modified. 
    if (ring == 'outer'):
        u_d_s[0], u_d_s[4] = u_d_s[4], u_d_s[0]
        u_d_s[1][0], u_d_s[3][0] = u_d_s[3][0], u_d_s[1][0]
        u_d_s[1][4], u_d_s[3][4] = u_d_s[3][4], u_d_s[1][4]
    if (ring == 'inner'):
        u_d_s[1][1:4], u_d_s[3][1:4] = u_d_s[3][1:4], u_d_s[1][1:4]
    return u_d_s

def left_right_flip(squarelotron, ring):
    """Performs the Left-Right Flip of the squarelotron."""
    l_r_s = deepcopy(squarelotron)
    if (ring == 'outer'):
        for row in range(5):
            l_r_s[row][0], l_r_s[row][4] = l_r_s[row][4], l_r_s[row][0]
        l_r_s[0][1], l_r_s[0][3] = l_r_s[0][3], l_r_s[0][1]
        l_r_s[4][1], l_r_s[4][3] = l_r_s[4][3], l_r_s[4][1]
    if (ring == 'inner'):
        for row in range(1, 4):
            l_r_s[row][1], l_r_s[row][3] = l_r_s[row][3], l_r_s[row][1]
    return l_r_s

def inverse_diagonal_flip(squarelotron, ring):
    """Performs the Main Inverse Diagonal of the squarelotron."""
    """i_d_s[row][column] -> i_d_s[4 - column][4 - row]"""
    i_d_s = deepcopy(squarelotron)
    if (ring == 'outer'):
        for column in range(4):
            i_d_s[0][column], i_d_s[4 - column][4] = i_d_s[4 - column][4], i_d_s[0][column]
        for row in range(1, 4):
            i_d_s[row][0], i_d_s[4][4 - row] = i_d_s[4][4 - row], i_d_s[row][0]
    if (ring == 'inner'):
        for column in range(1,3):
            i_d_s[1][column], i_d_s[4 - column][3] = i_d_s[4 - column][3], i_d_s[1][column]
        i_d_s[2][1], i_d_s[3][2] = i_d_s[3][2], i_d_s[2][1]
    return i_d_s

def main_diagonal_flip(squarelotron, ring):
    """Performs the Main Main Diagonal of the squarelotron."""
    """m_d_s[row][column] -> m_d_s[column][row]"""
    m_d_s = deepcopy(squarelotron)
    if (ring == 'outer'):
        for column in range(1, 5):
            m_d_s[0][column], m_d_s[column][0] = m_d_s[column][0], m_d_s[0][column]
        for row in range(1, 4):
            m_d_s[row][4], m_d_s[4][row] = m_d_s[4][row], m_d_s[row][4]
    if (ring == 'inner'):
        for column in range(2,4):
            m_d_s[1][column], m_d_s[column][1] = m_d_s[column][1], m_d_s[1][column]
        m_d_s[2][3], m_d_s[3][2] = m_d_s[3][2], m_d_s[2][3]
    return m_d_s

def rotated_squarelotron(squarelotron, rotate, ring):
    """Return the rotated squarelotron. It could also use the unnittest."""
    res = []
    if rotate == 'U':
        res = upside_down_flip(squarelotron, ring)
    if rotate == 'L':
        res = left_right_flip(squarelotron, ring)
    if rotate == 'I':
        res = inverse_diagonal_flip(squarelotron, ring)
    if rotate == 'M':
        res = main_diagonal_flip(squarelotron, ring)
    return res

# Use swap function later
#---------- Communicating with the user ----------

def print_instructions():
    print("""The Squarelotron game begin!
A Squarelotron consist basically of a matrix of numbers.This matrix can be decomposed as square rings which can rotate independently in 4 different ways:
Upside-Down (|), Left-Right (-), through the Inverse Diagonal (↙), and through the Main Diagonal (↘).
          """)

def print_Squarelotron(squarelotron):
    """Print the given squarelotron in a decent way."""
    print("\nThe Squarelotron!")
    print("\n-------------------------------------------------------------------------")
    for rows in squarelotron:
        for elements in rows:
            print(elements, end = '\t|\t')
        print("\n-------------------------------------------------------------------------")
    
def get_flip_rotate():
    """Ask user which kind of flip they want to make, return a string."""
    answer = input("""Which kind of flip you want to make?
You can type:
upside-down / u-d
left-right / l-r
inverse-diagnol / i-d
main-diagnol / m-d\n""")
    answer = answer.strip()
    if answer != "":
        user = answer.upper()[0]
        if user in {'U', 'L', 'I', 'M'}:
            return user 
        else:
            return get_flip_rotate()
    else:
        return get_flip_rotate()


def get_flip_ring():
    """Ask user which ring they want to rotate, return 'inner' or 'outer'."""
    answer = input("""Which ring you want to rotate?
You can type:
inner / i
outer / o\n""")
    answer = answer.strip()
    if answer != "":
        user = answer.upper()[0]
        if user == 'I':
            return ('inner')
        if user == 'O':
            return ('outer')
        else:
            return get_flip_ring()
    else:
        return get_flip_ring()

def play():
    """Ask user whether they want to play the game."""
    response = input("""\nDo you want to play the game?\n(any response that begins with 'y' or 'Y' means: yes, any response that begins with 'n' or 'N' means: no)\n""")
    # If the first character of the input string is 'Y' or 'y', play again
    if response[:1] == 'y' or response[:1] == 'Y':
        return True
    # If the first character of the input string is 'N' or 'n', print "Done"
    elif response[:1] == 'n' or response[:1] == 'N':
        return False
    # If the first character of the input string is anything else, ask the question again
    else:
        return play()
        
def main():
    l = [1, 2, 3, 4, 5,
         6, 7, 8, 9, 10,
         11, 12, 13, 14, 15,
         16, 17, 18, 19, 20,
         21, 22, 23, 24, 25]
    a = make_squarelotron(l)
    print_instructions()
    print_Squarelotron(a)
    while(play()): # When user want to play the game, do the following things.
        rotate = get_flip_rotate()
        ring = get_flip_ring()
        b = rotated_squarelotron(a, rotate, ring)
        a = b
        print_Squarelotron(b)
        
if __name__ == "__main__":
    main()
