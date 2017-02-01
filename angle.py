#!/usr/bin/python

#
#----This module is for calculating angle between three atoms whose coordinates are saved in A[]----
#

import numpy, sys, distance

def angles(A):
   a_a = A[0]
   b_a = A[1]
   c_a = A[2]
   D_ab = [a_a, b_a]
   ab = distance.dist(D_ab)
   D_bc = [b_a, c_a]
   bc = distance.dist(D_bc)
   D_ca = [c_a, a_a]
   ca = distance.dist(D_ca)
#   if ((ab <= 3.2700) and (bc <= 3.2700) and (ca <= 3.2700)):
   ab_2 = numpy.square(ab)
   bc_2 = numpy.square(bc)
   ca_2 = numpy.square(ca)
   a_ang_rad = numpy.arccos((ca_2 + ab_2 - bc_2)/(2.0 * ca * ab))
   a_ang_deg = numpy.degrees(a_ang_rad)
   b_ang_rad = numpy.arccos((ab_2 + bc_2 - ca_2)/(2.0 * ab * bc))
   b_ang_deg = numpy.degrees(b_ang_rad)
   c_ang_rad = numpy.arccos((bc_2 + ca_2 - ab_2)/(2.0 * bc * ca))
   c_ang_deg = numpy.degrees(c_ang_rad)
   ang = [a_ang_deg, b_ang_deg, c_ang_deg, ab, bc, ca]
   return ang
#   else:
#      dist = ['The O-O distance is not within the cutoff!!', ab, bc, ca]
#      return dist
