#!/usr/bin/env python3
import os
import sys


#converts a pdb with the format
#ATOM      1  N   MET     1       1.325   0.000   0.000  1.00  0.00      A
#ATOM      2  HT1 MET     1       1.746   0.686   0.658  1.00  0.00      A
#ATOM      3  HT2 MET     1       1.356  -0.949   0.423  1.00  0.00      A
#ATOM      4  HT3 MET     1       0.337   0.263  -0.189  1.00  0.00      A
#ATOM      5  CA  MET     1       2.073   0.000  -1.245  1.00  0.00      A
#ATOM      6  HA  MET     1       1.985   1.012  -1.640  1.00  0.00      A
#ATOM      7  CB  MET     1       3.533  -0.363  -0.964  1.00  0.00      A
#ATOM      8  HB1 MET     1       3.676  -0.302   0.140  1.00  0.00      A
#ATOM      9  HB2 MET     1       3.719  -0.331   0.109  1.00  0.00      A
#ATOM     10  CG  MET     1       4.484   0.597  -1.681  1.00  0.00      A

#to
#ATOM   1348  N   VAL A 190     133.624  28.918 -29.722  1.00 84.76           N       A
#ATOM   1349  CA  VAL A 190     132.770  28.797 -30.895  1.00 83.78           C       A
#ATOM   1350  C   VAL A 190     131.746  29.932 -30.954  1.00 84.41           C       A
#ATOM   1351  O   VAL A 190     131.602  30.701 -30.006  1.00 84.81           O       A
#ATOM   1352  CB  VAL A 190     132.023  27.449 -30.884  1.00 82.31           C       A
#ATOM   1353  CG1 VAL A 190     133.006  26.321 -30.641  1.00 81.31           C       A
#ATOM   1354  CG2 VAL A 190     130.947  27.454 -29.819  1.00 81.09           C       A
#ATOM   1355  N   GLU A 191     131.047  30.050 -32.077  1.00 84.62           N       A
#ATOM   1356  CA  GLU A 191     130.032  31.085 -32.211  1.00 84.39           C       A
#ATOM   1357  C   GLU A 191     128.850  30.643 -31.371  1.00 83.07           C       A

if len(sys.argv)!=3:
    print('Usage: [path-to-pdb] [path-to-outpdb]')
    quit()

data=open(sys.argv[1],'r').readlines()
data=[x.strip('\n').split() for x in data if x.startswith('ATOM')]

with open(sys.argv[2],'w') as of:
    for d in data:
        #print(d)
        outstr='ATOM'+d[1].rjust(7)+'  '+d[2].ljust(4)+d[3]+' '+d[10]+d[4].rjust(4)+d[5].rjust(12)+d[6].rjust(8)+d[7].rjust(8)+d[8].rjust(6)+d[9].rjust(6)+'\n'
        print(outstr)
        of.write(outstr)

