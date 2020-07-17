import math as m

#THE FOLLOWING COORDINATES ARE FOR RA
refCoor = 57368.84735444445
mean = 0.00806947
slope = 0.00000856959
period = 365.256
aSin1 = 0.000588361
bCos1 = 0.0000500055
c = 58209

RA_ECM_output = mean + bCos1 * m.cos((2 * m.pi * (c - refCoor))/period) + aSin1 * m.sin((2 * m.pi * (c - refCoor))/period) + slope * (c - refCoor)
print(RA_ECM_output)

#THE FOLLOWING COORDINATES ARE FOR DEC
refCoor = 57368.84735444445
mean = 0.0366658
slope = 0.0000184514
period = 365.256
aSin1 = 0.00596366
bCos1 = -0.00600029
c = 58209

Dec_ECM_output = mean + bCos1 * m.cos((2 * m.pi * (c - refCoor))/period) + aSin1 * m.sin((2 * m.pi * (c - refCoor))/period) + slope * (c - refCoor)
print(Dec_ECM_output)

