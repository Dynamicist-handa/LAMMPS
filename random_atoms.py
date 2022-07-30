#-----------------------------------------------------#
#Generate LAMMPS data file using random atom positions#
#             Rishab Handa, July 30, 2022             #
import numpy as np

#Number of atoms to create
natoms = 1000

#Size of the system cell in Angstroms
#assuming a cubic cell starting at the origin
sys_size = 20.0

#Generate atom positions
#Randomness for amorphous glass
position = []
for i in range(natoms):
    position.append(np.random.rand(3)*sys_size)

#LAMMPS data file
with open('random.data','w') as fdata:
    fdata.write('Random atoms simulation\n\n')

    #----HEADER----#
    #Specify the nr. of atoms and atom types
    fdata.write('{} atoms\n'.format(natoms))
    fdata.write('{} atom types\n'.format(1))

    #Specify box dimensions
    fdata.write('{} {} xlo xhi\n'.format(0.0, sys_size))
    fdata.write('{} {} ylo yhi\n'.format(0.0, sys_size))
    fdata.write('{} {} zlo zhi\n'.format(0.0, sys_size))
    fdata.write('\n')

    #Atoms section
    fdata.write('Atoms\n\n')

    #Write each position
    for pos in enumerate(position):
        fdata.write('{} 1 {} {} {}'.format(i+1, *pos))