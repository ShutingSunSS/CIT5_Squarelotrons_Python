# File:        Squarelotrons_test.py
# Programmer:  Shuting Sun
# Time:        Oct 2, 2016
# Description: CIT 590, Assignment 5.
#              The unittest of the file: Squarelotrons.py
          

from Squarelotrons import *   # import everything from your module
import unittest  # This loads the testing methods and a main program

class Squarelotrons(unittest.TestCase):
     def test_make_squarelotron(self):
        self.assertEqual(make_squarelotron([1]), [[1]])
        self.assertEqual(make_squarelotron([1, 2, 3, 4]), [[1, 2], [3, 4]])
        
        l = [1, 2, 3, 4, 5,
             6, 7, 8, 9, 10,
            11, 12, 13, 14, 15,
            16, 17, 18, 19, 20,
            21, 22, 23, 24, 25]
        self.assertEqual(make_squarelotron(l),\
                         [[1, 2, 3, 4, 5],
                          [6, 7, 8, 9, 10],
                          [11, 12, 13, 14, 15],
                          [16, 17, 18, 19, 20],
                          [21, 22, 23, 24, 25]])

     def test_make_list(self):
          self.assertEqual(make_list([[1]]), [1])
          self.assertEqual(make_list([[1, 2], [3, 4]]), [1, 2, 3, 4])
          self.assertEqual(make_list([[1], [2, 3]]), [1, 2, 3]) # can only concatenate list to list
          l = [[1, 2, 3, 4, 5],
               [6, 7, 8, 9, 10],
               [11, 12, 13, 14, 15],
               [16, 17, 18, 19, 20],
               [21, 22, 23, 24, 25]]
          self.assertEqual(make_list(l),\
                           [1, 2, 3, 4, 5,
                            6, 7, 8, 9, 10,
                           11, 12, 13, 14, 15,
                           16, 17, 18, 19, 20,
                           21, 22, 23, 24, 25])

     def test_upside_down_flip(self):
          l = [[1, 2, 3, 4, 5],
               [6, 7, 8, 9, 10],
               [11, 12, 13, 14, 15],
               [16, 17, 18, 19, 20],
               [21, 22, 23, 24, 25]]
          self.assertEqual(upside_down_flip(l, 'outer'),\
                           [[21, 22, 23, 24, 25],
                            [16, 7, 8, 9, 20],
                            [11, 12, 13, 14, 15],
                            [6, 17, 18, 19, 10],
                            [1, 2, 3, 4, 5]])
          self.assertEqual(upside_down_flip(l, 'inner'),\
                           [[1, 2, 3, 4, 5],
                            [6, 17, 18, 19, 10],
                            [11, 12, 13, 14, 15],
                            [16, 7, 8, 9, 20],
                            [21, 22, 23, 24, 25]])

     def test_left_right_flip(self):
          l = [[1, 2, 3, 4, 5],
               [6, 7, 8, 9, 10],
               [11, 12, 13, 14, 15],
               [16, 17, 18, 19, 20],
               [21, 22, 23, 24, 25]]
          self.assertEqual(left_right_flip(l, 'inner'),\
                           [[1, 2, 3, 4, 5],
                            [6, 9, 8, 7, 10],
                            [11, 14, 13, 12, 15],
                            [16, 19, 18, 17, 20],
                            [21, 22, 23, 24, 25]])
          self.assertEqual(left_right_flip(l, 'outer'),\
                           [[5, 4, 3, 2, 1],
                            [10, 7, 8, 9, 6],
                            [15, 12, 13, 14, 11],
                            [20, 17, 18, 19, 16],
                            [25, 24, 23, 22, 21]]) 
          
     def test_inverse_diagonal_flip(self):
          l = [[1, 2, 3, 4, 5],
               [6, 7, 8, 9, 10],
               [11, 12, 13, 14, 15],
               [16, 17, 18, 19, 20],
               [21, 22, 23, 24, 25]]
          self.assertEqual(inverse_diagonal_flip(l, 'inner'),\
                           [[1, 2, 3, 4, 5],
                            [6, 19, 14, 9, 10],
                            [11, 18, 13, 8, 15],
                            [16, 17, 12, 7, 20],
                            [21, 22, 23, 24, 25]])
          self.assertEqual(inverse_diagonal_flip(l, 'outer'),\
                           [[25, 20, 15, 10, 5],
                            [24, 7, 8, 9, 4],
                            [23, 12, 13, 14, 3],
                            [22, 17, 18, 19, 2],
                            [21, 16, 11, 6, 1]])
          
     def test_main_diagonal_flip(self):
          l = [[1, 2, 3, 4, 5],
               [6, 7, 8, 9, 10],
               [11, 12, 13, 14, 15],
               [16, 17, 18, 19, 20],
               [21, 22, 23, 24, 25]]
          self.assertEqual(main_diagonal_flip(l, 'inner'),\
                           [[1, 2, 3, 4, 5],
                            [6, 7, 12, 17, 10],
                            [11, 8, 13, 18, 15],
                            [16, 9, 14, 19, 20],
                            [21, 22, 23, 24, 25]])
          self.assertEqual(main_diagonal_flip(l, 'outer'),\
                           [[1, 6, 11, 16, 21],
                            [2, 7, 8, 9, 22],
                            [3, 12, 13, 14, 23],
                            [4, 17, 18, 19, 24],
                            [5, 10, 15, 20, 25]])
          
     def test_rotate_squarelotron(self):
          l = [[1, 2, 3, 4, 5],
               [6, 7, 8, 9, 10],
               [11, 12, 13, 14, 15],
               [16, 17, 18, 19, 20],
               [21, 22, 23, 24, 25]]
          self.assertEqual(rotated_squarelotron(l, 'U', 'inner'),\
                           [[1, 2, 3, 4, 5],
                            [6, 17, 18, 19, 10],
                            [11, 12, 13, 14, 15],
                            [16, 7, 8, 9, 20],
                            [21, 22, 23, 24, 25]])
          self.assertEqual(rotated_squarelotron(l, 'L', 'outer'),\
                          [[5, 4, 3, 2, 1],
                            [10, 7, 8, 9, 6],
                            [15, 12, 13, 14, 11],
                            [20, 17, 18, 19, 16],
                            [25, 24, 23, 22, 21]])
          self.assertEqual(rotated_squarelotron(l, 'I', 'inner'),\
                           [[1, 2, 3, 4, 5],
                            [6, 19, 14, 9, 10],
                            [11, 18, 13, 8, 15],
                            [16, 17, 12, 7, 20],
                            [21, 22, 23, 24, 25]])
          self.assertEqual(rotated_squarelotron(l, 'M', 'outer'),\
                           [[1, 6, 11, 16, 21],
                            [2, 7, 8, 9, 22],
                            [3, 12, 13, 14, 23],
                            [4, 17, 18, 19, 24],
                            [5, 10, 15, 20, 25]])
                            
unittest.main()
