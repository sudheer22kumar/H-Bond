#!/usr/bin/python

#
#-----This module figures out if the given set of "2 Oxygens and 1 Hydrogen" form hydrogen bond or not!!-------
#

import numpy, sys, angle, angle_sort

def hbond(A, h, o, bond_cutoff, angle_cutoff): #---A is the list of three atoms (2 'O' and 1 'H'), 'h' gives which one of these atoms is 'H' and 'o' tells me which one of the oxygens is attached to the hydrogen.-----
#    bond_cutoff = 2.8
#    angle_cutoff = 20.0
    if (h == 1 and o == 2):
        H = A[0]
        O1 = A[1]
        O2 = A[2]
    if (h == 1 and o == 3):
        H = A[0]
        O1 = A[2]
        O2 = A[1]
    if (h == 2 and o == 1):
        H = A[1]
        O1 = A[0]
        O2 = A[2]
    if (h == 2 and o == 3):
        H = A[1]
        O1 = A[2]
        O2 = A[0]
    if (h == 3 and o == 1):
        H = A[2]
        O1 = A[0]
        O2 = A[1]
    if (h == 3 and o == 2):
        H = A[2]
        O1 = A[1]
        O2 = A[0]
    
#    HO2 = [H, O2]
#    HO2_dist = distance.dist(HO2)

    OHO = [O1, H, O2]
    angle_OHO = angle.angles(OHO)
    OHO_angle = angle_sort.ang_sort(2 , angle_OHO)
    HO1O_angle = angle_sort.ang_sort(1, angle_OHO)
    HO2_dist = angle_sort.dist_sort(2, 3, angle_OHO)

    if (HO2_dist <= bond_cutoff and HO1O_angle <= angle_cutoff):
        return "True", HO2_dist, HO1O_angle, bond_cutoff, angle_cutoff
    else:
        return "False", HO2_dist, HO1O_angle, bond_cutoff, angle_cutoff

