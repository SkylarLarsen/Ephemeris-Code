import math

Obs_RA = 261.0971727
Obs_Dec = -1.8499347
Calc_RA_hrs = 17
Calc_RA_min = 24
Calc_RA_sec = 23.32
Calc_Dec_hrs = -1
Calc_Dec_min = 50
Calc_Dec_sec = 59.7

Decimal_Calc_RA = (Calc_RA_hrs + Calc_RA_min/60 + Calc_RA_sec/3600) * 15
Decimal_Calc_Dec = abs(Calc_Dec_hrs) + Calc_Dec_min/60 + Calc_Dec_sec/3600

if Calc_Dec_hrs < 0:
    Decimal_Calc_Dec = -Decimal_Calc_Dec

print("Calculated RA:", Decimal_Calc_RA)
print("Calculated Dec:", Decimal_Calc_Dec)

OC_RA = abs((Obs_RA - Decimal_Calc_RA) * math.cos(Decimal_Calc_Dec*(math.pi/180)))
OC_Dec = abs(Obs_Dec - Decimal_Calc_Dec)

print("Calculated RA Ephemeris:", OC_RA)                 #In Decimal Degrees
print("Calculated Dec Ephemeris:", OC_Dec)               #In Decimal Degrees
print("RA Ephemeris in arcseconds:", OC_RA * 3600)
print("Dec Ephemeris in arcseconds:", OC_Dec * 3600)
