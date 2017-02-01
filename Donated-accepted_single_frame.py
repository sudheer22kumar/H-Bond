#!/usr/bin/python
#
# Sudheer of PRG.
#

import numpy, sys, distance, angle, angle_sort, hbonds
from os import path

if len(sys.argv) > 1:
   trajectory_name = sys.argv[1]
else:
   sys.exit("USAGE: python Snap_Select.py <Trajectory> (or) ./Snap_Select.py <Trajectory>\n")

print "H-Bond Distance Cutoff: "
bond_cutoff = float(raw_input())

print "H-Bond Angle(HOO) Cutoff: "
angle_cutoff = float(raw_input())

traj_split = path.basename(trajectory_name)
traj_dir   = path.dirname(path.abspath(trajectory_name))
trajectory = traj_split.split('.')[0]

traj     = file(traj_dir+'/'+trajectory+'.xyz', "r")
traj_pbc = file(trajectory+'_pbc.xyz', "w")
lines = traj.readlines()

steps     = []
atoms     = []
x_dir     = []
x_dir_pbc = []
y_dir     = []
y_dir_pbc = []
z_dir     = []
z_dir_pbc = []
atoms_O   = []
atoms_H   = []
x_O       = []
x_O_pbc   = []
y_O       = []
y_O_pbc   = []
z_O       = []
z_O_pbc   = []
x_H       = []
x_H_pbc   = []
y_H       = []
y_H_pbc   = []
z_H       = []
z_H_pbc   = []
oxygens   = []
hydrogens = []
oxy_angle = []
box_len   = 12.4278

#
#-------Saving Coordinates in different variables---------
#

for i in range(0,len(lines)):
   line = lines[i]
   if (line[0] == ' '):
      traj_pbc.write(line)
   if (line[0] == '#'):
      steps_1 = line.split()
      step = steps_1[0]+" "+steps_1[1]+"\t"+steps_1[2]
      steps.append(step) #-----Number of Steps.
      traj_pbc.write(line)
   if (line[0] == 'O'):
      chunk = line.split()
      atoms.append(chunk[0])
      atoms_O.append(chunk[0])
      
      x_dir.append(float(chunk[1]))
      O_pbc_x = float(chunk[1]) - (box_len * numpy.floor(float(chunk[1])/box_len))
      O_pbc_x_move = O_pbc_x - float(chunk[1])
      x_dir_pbc.append(O_pbc_x)
      
      y_dir.append(float(chunk[2]))
      O_pbc_y = float(chunk[2]) - (box_len * numpy.floor(float(chunk[2])/box_len))
      O_pbc_y_move = O_pbc_y - float(chunk[2])
      y_dir_pbc.append(O_pbc_y)
      
      z_dir.append(float(chunk[3]))
      O_pbc_z = float(chunk[3]) - (box_len * numpy.floor(float(chunk[3])/box_len))
      O_pbc_z_move = O_pbc_z - float(chunk[3])
      z_dir_pbc.append(O_pbc_z)
      
      #            traj_pbc.write("%s\t%2.9f  %2.9f  %2.9f  %2.9f  %2.9f  %2.9f\n" % (chunk[0], O_pbc_x, O_pbc_y, O_pbc_z, float(chunk[4]), float(chunk[5]), float(chunk[6])))
      
      traj_pbc.write("%s\t%f\t%f\t%f\n" % (chunk[0], O_pbc_x, O_pbc_y, O_pbc_z))
      
      x_O.append(float(chunk[1]))
      y_O.append(float(chunk[2]))
      z_O.append(float(chunk[3]))
      x_O_pbc.append(O_pbc_x)
      y_O_pbc.append(O_pbc_y)
      z_O_pbc.append(O_pbc_z)
      
   if (line[0] == 'H'):
      chunk = line.split()
      atoms.append(chunk[0])
      atoms_H.append(chunk[0])
      
      x_dir.append(float(chunk[1]))
      H_pbc_x = float(chunk[1]) + O_pbc_x_move
      x_dir_pbc.append(H_pbc_x)
      
      y_dir.append(float(chunk[2]))
      H_pbc_y = float(chunk[2]) + O_pbc_y_move
      y_dir_pbc.append(H_pbc_y)
      
      z_dir.append(float(chunk[3]))
      H_pbc_z = float(chunk[3]) + O_pbc_z_move
      z_dir_pbc.append(H_pbc_z)
      
      #traj_pbc.write("%s\t%2.9f  %2.9f  %2.9f  %2.9f  %2.9f  %2.9f\n" % (chunk[0], H_pbc_x, H_pbc_y, H_pbc_z, float(chunk[4]), float(chunk[5]), float(chunk[6])))
      
      traj_pbc.write("%s\t%f\t%f\t%f\n" % (chunk[0], H_pbc_x, H_pbc_y, H_pbc_z))
      
      x_H.append(float(chunk[1]))
      y_H.append(float(chunk[2]))
      z_H.append(float(chunk[3]))
      x_H_pbc.append(H_pbc_x)
      y_H_pbc.append(H_pbc_y)
      z_H_pbc.append(H_pbc_z)
      
traj.close()
traj_pbc.close()


#
#-------End of coordinates being saved in different variables!!---------
#

#
#-------Saving Coordinates stepwise!!---------
#

#for stp in range(0,len(steps)):
for o_stp in range(1, 65):
   stp = 0
   oxy = atoms_O[(stp * 64) + o_stp - 1]
   oxy_x = x_O_pbc[(stp * 64) + o_stp - 1]
   oxy_y = y_O_pbc[(stp * 64) + o_stp - 1]
   oxy_z = z_O_pbc[(stp * 64) + o_stp - 1]
   #      oxygen = [stp, o_stp, oxy, oxy_x, oxy_y, oxy_z]
   oxygen = [o_stp, oxy, oxy_x, oxy_y, oxy_z]
   oxygens.append(oxygen)
   for h_stp in range(1, 3):
      hyd = atoms_H[(stp * 128) + (2 * o_stp) + h_stp - 3]
      hyd_x = x_H_pbc[(stp * 128) + (2 * o_stp) + h_stp - 3]
      hyd_y = y_H_pbc[(stp * 128) + (2 * o_stp) + h_stp - 3]
      hyd_z = z_H_pbc[(stp * 128) + (2 * o_stp) + h_stp - 3]
      #         hydrogen = [stp, o_stp, hyd, h_stp, hyd_x, hyd_y, hyd_z]
      hydrogen = [o_stp, hyd, h_stp, hyd_x, hyd_y, hyd_z]
      hydrogens.append(hydrogen)

#coord1 = file("Coordinates_org.txt", "w")
#
#for j in range(1, 65):
#   i = 0
#   coord1.write("%s\t%f\t%f\t%f\n" % (oxygens[(i * 64) + j - 1][1], oxygens[(i * 64) + j - 1][2], oxygens[(i * 64) + j - 1][3], oxygens[(i * 64) + j - 1][4]))#, oxygens[(i * 64) + j - 1][5]))
#   for k in range(1, 3):
#      coord1.write("%s\t%f\t%f\t%f\n" % (hydrogens[(i * 128) + (2 * j) + k - 3][1], hydrogens[(i * 128) + (2 * j) + k - 3][3], hydrogens[(i * 128) + (2 * j) + k - 3][4], hydrogens[(i * 128) + (2 * j) + k - 3][5]))#, hydrogens[(i * 128) + (2 * j) + k - 3][6]))         
#
#coord1.close()

#
#-------Creating Periodic Images----------#
#
      
for x in [0, 1, -1]:
   for y in [0, 1, -1]:
      for z in [0, 1, -1]:
         #for stp in range(0,len(steps)):
         if (x == 0 and y == 0 and z == 0):
            sudheer = 1
         else:
            for o_stp in range(1, 65):
               stp = 0
               oxy = atoms_O[(stp * 64) + o_stp - 1]
               oxy_x = x_O_pbc[(stp * 64) + o_stp - 1] + (x * 12.4278)
               oxy_y = y_O_pbc[(stp * 64) + o_stp - 1] + (y * 12.4278)
               oxy_z = z_O_pbc[(stp * 64) + o_stp - 1] + (z * 12.4278)
               oxygen = [o_stp, oxy, oxy_x, oxy_y, oxy_z]
               oxygens.append(oxygen)
               for h_stp in range(1, 3):
                  hyd = atoms_H[(stp * 128) + (2 * o_stp) + h_stp - 3]
                  hyd_x = x_H_pbc[(stp * 128) + (2 * o_stp) + h_stp - 3] + (x * 12.4278)
                  hyd_y = y_H_pbc[(stp * 128) + (2 * o_stp) + h_stp - 3] + (y * 12.4278)
                  hyd_z = z_H_pbc[(stp * 128) + (2 * o_stp) + h_stp - 3] + (z * 12.4278)
                  hydrogen = [o_stp, hyd, h_stp, hyd_x, hyd_y, hyd_z]
                  hydrogens.append(hydrogen)

#
#-------End of stepwise saving of coordinates!!-------
#


#
#-------Distance and Angle Determination--------#
#


#for i in range(0, len(steps)):
i = 0
Ohbond_list = []
for j in range(1, 65):
    li = [j, 0, 0]
    Ohbond_list.append(li)

Ohbond_file = file("HBonds_Number.txt", "w")
Total_hbond = 0
for j in range(1, 65):
   hlist = []
   Ohbond = 0
   OXY_A = [oxygens[j - 1][2], oxygens[j - 1][3], oxygens[j - 1][4]]
   oxy_range = range(1, len(oxygens) + 1)
   oxy_range.remove(j)
   for k in range(1, 3):
       HYD_A = [hydrogens[(2 * j) + k - 3][3], hydrogens[(2 * j) + k - 3][4], hydrogens[(2 * j) + k - 3][5]]
       for l in oxy_range:
           OXY_B = [oxygens[l - 1][2], oxygens[l - 1][3], oxygens[l - 1][4]]
           A = [OXY_A, HYD_A, OXY_B]
           answer_hbond, hbond_dist, hbond_angle, hbond_cutoff, hangle_cutoff = hbonds.hbond(A, 2, 1, bond_cutoff, angle_cutoff)
           if (answer_hbond == "True"):
               Ohbond = Ohbond + 1
               Ohbond_list[j - 1][1] = Ohbond_list[j - 1][1] + 1
           if (answer_hbond == "True" and l < 65):
               Ohbond_list[l - 1][2] = Ohbond_list[l - 1][2] + 1
   Total_hbond = Total_hbond + Ohbond


Ohbond_file.write("%i  %f  Bond Cutoff = %2.3f  Angle Cutoff = %3.3f\n\n" % (Total_hbond, Total_hbond/64.0, hbond_cutoff, hangle_cutoff))
for j in range(1, 65):
    Ohbond_file.write("%i\t%i\t%i\t%i\n" % (j, Ohbond_list[j - 1][1], Ohbond_list[j - 1][2], Ohbond_list[j - 1][1] + Ohbond_list[j - 1][2]))
Ohbond_file.close()

