import astropy
import astropy.timeseries
import astropy.units as u
import numpy as np
import matplotlib.pyplot as plt
import math as m
from astropy.timeseries import LombScargle 

refCoor = 57368.84735444445
mean = 0.00806947
slope = 0.00000856959
period = 365.256
aSin1 = 0.000588361
bCos1 = 0.0000500055

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
    ECM_point = mean + bCos1 * m.cos((2 * m.pi * (c - refCoor))/period) + aSin1 * m.sin((2 * m.pi * (c - refCoor))/period) + slope * (c - refCoor)
    #print(ECM_point)
    ECM_output.append(ECM_point)
#print(ECM_output)
#plt.scatter(t, ECM_output)             #Should make a nice sine wave

y = (0.019700964,0.005330343,-0.015574847,0.019611893,                                                                                                                                  #Feb 05 2018
     0.009801373,0.04464851,0.028848677,0.092333545,0.045652022,0.017955704,-0.034562498,                                                                                               #Feb 06 2018
     0.013250873,0.011534755,0.017854068,0.014816631,0.015752207,0.018836688,0.015109028,0.021118319,0.017049733,0.018034366,                                                           #Mar 21 2018
     0.016299855,0.033968376,0.033360634,0.031710944,0.046895672,0.03542277,0.032232841,0.038762065,0.038520112,0.023789836,0.033554919,0.031793879,                                    #May 09 2018
     0.025856138,0.019959983,0.027618929,0.023760462,0.034709688,                                                                                                                       #May 10 2018
     0.0042935,0.016495533,0.017908631,-0.00948188,0.003833242,0.017518804,0.00996887,-0.000832808,                                                                                     #May 12 2018
     0.040954849,0.011263265,0.025338746,0.038691202,0.043052806,0.021839305,0.030171393,0.038862388,                                                                                   #Jun 03 2018
     0.018407652,0.00629502,0.00729221,0.008648885,0.011450977,0.011010798,0.01525751,0.013380539,0.014559521,0.005843508,0.012979549,                                                  #Jun 05 2018
     0.024728872,0.036273421,0.015202127,0.029792393,0.025655899,0.035207774,0.028911357,0.030191273,0.027863009,0.039583001,                                                           #Jun 08 2018
     0.021392631,0.01525171,0.02487741,0.021903149,0.027936227,0.025328311,0.017312609,0.017229018,0.025082958,0.024999476,0.024479765,0.03125357,0.028305361,0.029681644,0.017005508,  #Jun 09 2018
     -0.004558,0.002646319,0.01345022,0.017411344,-0.002032618,0.005178896,0.003028991,0.004483653,0.001690466,-0.001165458,                                                            #Jun 10 2018
     -0.015323266,-0.005968882,                                                                                                                                                         #Jul 10 2018
     -0.030478851,0.021228934,-0.019094853,0.010133696,-0.010754913,0.015408357,-0.001298706,0.058098839,0.004632478,0.150216262,                                                       #Aug 14 2018
     -0.012578686,0.011021326,0.020319181,0.025867137,0.045784882,0.026711231,0.029753468,0.049067701,0.03396304,0.048584068,0.039591731,0.025398775,0.021523006,0.027002724,           #Aug 16 2018
     0.013719843,0.021253147,0.002091306,0.012105585,0.020159037,0.015398613,0.013157587,0.010605491,0.017362698,0.010068055,0.002029058,0.009138712,0.011562855,0.026113569,           #Sep 01 2018
     0.013462963,0.014084694,0.006056617,0.002706489,0.00259593,-0.001121339,0.028297048,0.016285093,0.022278964,0.026108404,0.011630917,0.04822923,-0.004152908,0.017307873,-0.001942244)  #"


#Plotting raw data
plt.scatter(t,y)              

#Subtracting the ECM funcitonal form from the raw data
data = []
zip_object = zip(y, ECM_output)
for y_i, ECM_output_i in zip_object:
    data.append(y_i-ECM_output_i)
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