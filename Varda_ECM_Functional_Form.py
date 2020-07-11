import math as m

#mean + aSin1 Cos[(2 Pi (c - refCoor))/period] + bCos1 Cos[(4 Pi (c - refCoor))/period] + 
#aSin1 Sin[(2 Pi (c - refCoor))/period] + bCos1 Sin[(4 Pi (c - refCoor))/period] + slope (c - refCoor)

#THE FOLLOWING COORDINATES ARE FOR RA
refCoor = 57371.3
mean = 0.00812197
slope = -0.0000123731
period = 365.256
aSin1 = 0.00403133
bCos1 = -0.000433795
c = 58369.14741055555

RA_ECM_output = mean + aSin1 * m.cos((2 * m.pi * (c - refCoor))/period) + bCos1 * m.cos((4 * m.pi * (c - refCoor))/period) + aSin1 * m.sin((2 * m.pi * (c - refCoor))/period) + bCos1 * m.sin((4 * m.pi * (c - refCoor))/period) + slope * (c - refCoor)
print(RA_ECM_output)

#THE FOLLOWING COORDINATES ARE FOR DEC
refCoor = 57371.3
mean = 0.0646109
slope = 0.0000391309
period = 365.256
aSin1 = 0.0143764
bCos1 = -0.00787495
c = 58369.14741055555

Dec_ECM_output = mean + aSin1 * m.cos((2 * m.pi * (c - refCoor))/period) + bCos1 * m.cos((4 * m.pi * (c - refCoor))/period) + aSin1 * m.sin((2 * m.pi * (c - refCoor))/period) + bCos1 * m.sin((4 * m.pi * (c - refCoor))/period) + slope * (c - refCoor)
print(Dec_ECM_output)

