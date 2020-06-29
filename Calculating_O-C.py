import math

Obs_RA =            #Observed RA from mpc file here
Obs_Dec =           #Observed Dec "
Calc_RA_hrs =       #RA hours from JPL Horizons Database here
Calc_RA_min =       #RA minutes "
Calc_RA_sec =       #RA seconds "
Calc_Dec_hrs =      #Dec degrees "
Calc_Dec_min =      #Dec arcminutes "
Calc_Dec_sec =      #Dec arcseconds "

#Convert Calculated RA and Dec from hrs min sec
#or degrees arcmin arcsec to decimal degrees:
Decimal_Calc_RA = (Calc_RA_hrs + Calc_RA_min/60 + Calc_RA_sec/3600) * 15
Decimal_Calc_Dec = abs(Calc_Dec_hrs) + Calc_Dec_min/60 + Calc_Dec_sec/3600

if Calc_Dec_hrs < 0:
    Decimal_Calc_Dec = -Decimal_Calc_Dec

print("Calculated RA:", Decimal_Calc_RA)
print("Calculated Dec:", Decimal_Calc_Dec)

#Calculate Difference between observed vs. Calculated RA and Dec
OC_RA = (Obs_RA - Decimal_Calc_RA) * math.cos(Decimal_Calc_Dec*(math.pi/180))
OC_Dec = Obs_Dec - Decimal_Calc_Dec

print("Calculated RA Ephemeris:", OC_RA)                 #In Decimal Degrees
print("Calculated Dec Ephemeris:", OC_Dec)               #In Decimal Degrees
print("RA Ephemeris in arcseconds:", OC_RA * 3600)       #In Arcseconds
print("Dec Ephemeris in arcseconds:", OC_Dec * 3600)     #In Arcseconds
