#!/usr/bin/python

#
#-----This module will give correct angle based on the central atom given by Cen_atom and list of angles-----
#

import numpy, sys

def ang_sort(Cen_atom, ang):
    if (Cen_atom == 1):
        return ang[0]
    elif (Cen_atom == 2):
        return ang[1]
    elif (Cen_atom == 3):
        return ang[2]
    else:
        print "There cannot be more than 3 atoms for angle determination!!"

def dist_sort(Atom_1, Atom_2, ang):
    if ((Atom_1 == 1 and Atom_2 == 2) or (Atom_1 == 2 and Atom_2 == 1)):
        return ang[3]
    elif ((Atom_1 == 1 and Atom_2 == 3) or (Atom_1 == 3 and Atom_2 == 1)):
        return ang[5]
    elif ((Atom_1 == 2 and Atom_2 == 3) or (Atom_1 == 3 and Atom_2 == 2)):
        return ang[4]
    else:
        print "There cannot be more than 3 bonds for water molecule!!"
