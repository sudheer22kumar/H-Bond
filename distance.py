#!/usr/bin/python

#
#----This module is for calculating distance between two atoms whose coordinates are saved in A[][]----
#

import numpy, sys

def dist(A):
   a_x = A[0][0]
   a_y = A[0][1]
   a_z = A[0][2]
   b_x = A[1][0]
   b_y = A[1][1]
   b_z = A[1][2]
   d = numpy.sqrt(numpy.square(b_x - a_x) + numpy.square(b_y - a_y) + numpy.square(b_z - a_z))
   return d
