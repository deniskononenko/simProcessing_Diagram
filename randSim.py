#!/usr/bin/python3

import os





def genInp():
	fid = open('helix.inp', 'w')
	fid.write("""#
# Geometry
#
geometry = curved
a = 1
b = 1
h = 2000
geomFile = "../afmHelixGeom.dat"
#
##############################################
# Magnetic parameters
# 
damping = 0.5
J0 = -1.0
muB = 1.
dipInteraction = off
aniAxis = on
aniAxisFile = "../afmHelixAnisotropy.dat"
aniAxisCoef = -0.0204
#
##############################################
# Initial distribution
#
init = random
#initFile = "./afmHelixInitDistr.dat"
#
##############################################
# Magnetic field
#fieldZ = select t > -1.0 const -0.6 0
#
##############################################
# Integration 
# 
timeStep = 300.0
snapshotCount = 300
stopdMdt = -1
volumeModel = 3D
tolerance = 1e-2
intStepCount = 800
scanx1 = 0
scany1 = 0
scanz1 = 150""")
	fid.close()

def main():
	#cur = [0.005, 0.2, 0.4, 0.6, 0.8, 1]
	cur = [0.8, 1]
	tor = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7]

	#path = str(os.getcwd())
	path = os.getcwd()
	print(os.getcwd())
	#path = str(os.getcwd())
	for k in cur:
		for s in tor:
			os.chdir(path + '/' + 'k' + str(k) +'s'+ str(s))
			print(os.getcwd())
			os.mkdir('r')
			os.chdir('r')
			genInp()
			#os.rename("../" + sim + "-afmHelixInitDistr.dat", "./afmHelixInitDistr.dat")
			os.system('timeout 550s /opt/slasi/slasi helix.inp -n --no-verbose')
			os.chdir('..')

if __name__ == "__main__":
	main()

