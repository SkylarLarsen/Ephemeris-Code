import astropy
import astropy.timeseries
import astropy.units as u
import numpy as np
import matplotlib.pyplot as plt
import math as m
from astropy.timeseries import LombScargle 

refCoor = 57371.3
mean = 0.0646109
slope = 0.0000391309
period = 365.256
aSin1 = 0.0143764
bCos1 = -0.00787495

t = (58154.51741503,58154.52006401,58154.52249801,58154.52450822,                                                                        #Feb 05 2018
     58155.55294107,58155.55474757,58155.5564104,58155.55807328,58155.55978149,58155.56144503,58155.56310799,                            #Feb 06 2018
     58198.45563286,58198.45760036,58198.45926344,58198.4609264,58198.46258936,58198.46432915,58198.46599211,58198.46765511,             #Mar 21 2018
     58198.46931807,58198.47098115,                                                                                                      #"                                                           
     58245.44644411,58245.44823844,                                                                                                      #May 07 2018
     58247.46065024,58247.46245057,58247.46411353,58247.46577649,58247.46743949,58247.46910244,58247.4708279,58247.47249086,             #May 09 2018
     58247.47415394,58247.47581711,                                                                                                      #"                                                                  
     58248.35267674,58248.35464374,58248.35630669,58248.35796969,58248.35963332,                                                         #May 10 2018
     58250.36650974,58250.36840719,58250.37007003,58250.37173299,58250.37339594,58250.37665682,58250.37832003,58250.37998299,            #May 12 2018
     58272.27288403,58272.27473832,58272.2764014,58272.27806436,58272.27972744,58272.2813904,58272.2831809,58272.28484386,               #Jun 03 2018
     58274.25946214,58274.26162985,58274.26259839,58274.26356689,58274.26453543,58274.26550393,58274.26647247,58274.26744097,            #Jun 05 2018
     58274.26862697,58274.26959547,58274.27056401,                                                                                       #"
     58277.28057292,58277.28239504,58277.28371075,58277.2850265,58277.28634225,58277.287658,58277.28897371,58277.29028958,58277.29160533,#Jun 08 2018
     58277.29292108,                                                                                                                     #"                                                                    
     58278.25700996,58278.25857837,58278.25989408,58278.26120983,58278.26252558,58278.26384133,58278.26515696,58278.26647267,            #Jun 09 2018
     58278.26778854,58278.26910417,58278.27068633,58278.27200208,58278.27331783,58278.27463358,58278.27594921,                           #"                                      
     58279.25367338,58279.25568808,58279.25700383,58279.25831954,58279.25963529,58279.26095104,58279.26226679,58279.26358254,            #Jun 10 2018
     58279.26508496,58279.26640079,                                                                                                      #"                                                                       
     58309.30658821,58309.30897317,                                                                                                      #Jul 10 2018
     58344.15521343,58344.18049167,58344.1836125,58344.28287512,58344.2844455,58344.286039,58344.28735462,58344.28873021,                #Aug 14 2018
     58344.29004583,58344.29145383,                                                                                                      #"                                                                       
     58346.12774342,58346.12985394,58346.13161111,58346.13330265,58346.13505244,58346.13675394,58346.13846157,58346.14017199,            #Aug 16 2018
     58346.14194894,58346.14395786,58346.14567511,58346.14867015,58346.15039107,58346.15208194,                                          #"
     58362.11826668,58362.11946935,58362.12043772,58362.12140614,58362.12264435,58362.12361272,58362.12458114,58362.12654664,            #Sep 01 2018
     58362.12751506,58362.12848335,58362.12952314,58362.13049156,58362.13145997,58362.20557222,58362.20671735,58362.20768576,            #"
     58362.20865418,58362.20962247,58362.21059122,58362.21155997,58362.2125286,58362.21349722,58362.21446564,58362.21543439,             #"
     58362.21658601,58362.21755439,58362.21852268,58362.21949131,58362.22045972)              

#putting data through the ECM functional form
ECM_output= []
for i in t:
    c = i
    ECM_point = mean + aSin1 * m.cos((2 * m.pi * (c - refCoor))/period) + bCos1 * m.cos((4 * m.pi * (c - refCoor))/period) + aSin1 * m.sin((2 * m.pi * (c - refCoor))/period) + bCos1 * m.sin((4 * m.pi * (c - refCoor))/period) + slope * (c - refCoor)
    #print(ECM_point)
    ECM_output.append(ECM_point)
#print(ECM_output)
#plt.scatter(t, ECM_output)             #Should make a nice sine wave

y = (-0.029538,-0.027979,-0.033455,-0.019879,                                                                                                           #Feb 05 2018
      -0.044316,0.004961,-0.039359,-0.045875,-0.039380,-0.036536,0.033988,                                                                              #Feb 06 2018
      -0.001346,0.003546,0.019210,0.004122,0.015671,0.013432,-0.002736,0.003928,0.002516,0.002516,                                                      #Mar 21 2018
      -0.006674,-0.050180,                                                                                                                              #May 07 2018
      -0.024491,-0.021035,-0.017060,-0.019562,-0.016819,-0.019325,-0.014425,-0.015487,-0.020873,-0.021215,                                              #May 09 2018
      -0.006890,-0.003031,-0.004403,-0.009166,-0.002412,                                                                                                #May 10 2018
       0.041342,-0.012442,-0.009490,0.019177,0.003409,-0.002099,-0.003467,-0.021960,                                                                    #May 12 2018
      -0.004730,0.006178,0.002228,-0.016326,-0.001919,-0.003193,0.010699,-0.007290,                                                                     #Jun 03 2018
      -0.003046,0.001638,0.008507,0.001336,0.004453,0.000162,0.003791,-0.012020,0.001120,0.014828,0.002257,                                             #Jun 05 2018
      -0.000652,-0.003719,0.010760,0.000756,-0.002045,-0.003766,-0.004255,-0.014256,0.000580,-0.015901,                                                 #Jun 08 2018
       0.014162,0.005803,0.008658,-0.000004,0.003571,0.012910,0.013968,0.006178,0.004352,0.000011,0.000652,0.005310,0.010325,-0.008057,0.016758,        #Jun 09 2018
      -0.002984,0.004442,0.003391,0.000025,-0.001897,-0.011743,0.013846,0.015523,0.010562,0.010436,                                                     #Jun 10 2018
      -0.009364,-0.027263,                                                                                                                              #Jul 10 2018
      -0.018346,-0.038351,0.010991,-0.010656,0.061128,0.071759,-0.002581,-0.005692,-0.043312,0.093722,                                                  #Aug 14 2018
      -0.007830,0.003301,0.001706,-0.011927,-0.011002,-0.007146,-0.007974,-0.004273,-0.015689,0.003766,-0.016088,0.005584,-0.023990,-0.012269,          #Aug 16 2018
      -0.019494,-0.005170,-0.001656,-0.014191,-0.018274,-0.026845,-0.022255,-0.034258,-0.026633,-0.014123,-0.020480,-0.027767,-0.005742,                #Sep 01 2018
       0.010350,-0.022280,-0.052456,-0.008262,-0.038437,-0.027007,-0.022262,-0.023789,-0.021564,-0.000770,0.002380,-0.048611,-0.026586,-0.036032,       #"
      -0.034168,-0.043258)


#Plotting raw data
plt.scatter(t,y)              

#Subtracting the ECM funcitonal form from the raw data
data = []
zip_object = zip(y, ECM_output)
for y_i, ECM_output_i in zip_object:
    data.append(y_i-(ECM_output_i))
#print(data)
#plt.scatter(t,data)   #Plotting Raw Data - ECM functional form graph

### Preparation of Data ############################################################################################
### Frequency
ls = LombScargle(t, data)
frequency, power = ls.autopower(nyquist_factor=500,minimum_frequency=0.2)

### Units
period_days = 1 / frequency
period_hours = period_days * 24

best_period = period_days[np.argmax(power)]
phase = (t / best_period) % 1
print("Best period: {0:.2f} hours".format(24 * best_period))
#print(phase)
#plt.scatter(phase, y)

### Lomb-Scargle Model ############################################################################################
fig, ax = plt.subplots(figsize=(10, 3))

phase_model = np.linspace(-0.5, 1.5, 100)
best_frequency = frequency[np.argmax(power)]
mag_model = ls.model(phase_model / best_frequency, best_frequency)

for offset in [-1, 0, 1]:
    ax.errorbar(phase + offset, data, fmt='.',
                color='gray', ecolor='lightgray', capsize=0);
ax.plot(phase_model, mag_model, '-k', lw=2)
ax.set(xlim=(0, 1),
       xlabel='phase',
       ylabel='difference')
ax.invert_yaxis()
