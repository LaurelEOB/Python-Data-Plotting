# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 14:25:10 2024

@author: bloss
"""

import glob
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.options.display.max_rows = 999


if __name__ == "__main__":
    dataFiles = glob.glob('/Users/bloss/OneDrive/documents/DataSets/RS41_Flight_from_SD/*.csv')
    
    dataFrames = []
    
    for fileName in dataFiles:
       df = pd.read_csv(fileName, index_col=None, header=0) 
       dataFrames.append(df)
        
    fullData = pd.concat(dataFrames, ignore_index=True)
    
    #fullData = fullData[0:500]
    
    timeData = fullData.get("Time")
    
    timeHours = []
    timeMin = []
    timeSec = []
    for times in timeData:
        timePlace = str(times)
        timeHours.append(int(timePlace[8:10]))
        timeMin.append(int(timePlace[10:12]))
        timeSec.append(int(timePlace[12:14]))
        
        
    timeDataNew = (pd.Series(timeHours)*3600) + (pd.Series(timeMin)*60) + (pd.Series(timeSec))
    timeDataNew = timeDataNew / 3600 # Time in hours


    fig1, ax1 = plt.subplots()
    plt.title("RS41 data, Sweden Flight")
    
    colorA1 = 'tab:red'
    ax1.set_xlabel('time [hours]')
    ax1.set_ylabel('External Air Temp [deg C]', color=colorA1)
    ax1.plot(timeDataNew, fullData.get("hsensor_temp_degC"),"o",ms=1,color=colorA1)
    ax1.plot(timeDataNew, fullData.get("pcb_heater_on"),"o",ms=1,color="tab:orange")
    ax1.tick_params(axis='y', labelcolor=colorA1)
    
    ax2 = ax1.twinx()

    colorA2 = 'tab:blue'
    ax2.set_ylabel('RS41 Internal Temp [deg C]', color=colorA2)
    ax2.plot(timeDataNew, fullData.get("lsm303_temp_degC"),"o",ms=1,color=colorA2)
    ax2.tick_params(axis='y', labelcolor=colorA2)
    
    
    fig2, ax3 = plt.subplots()
    ax3.plot(timeDataNew, fullData.get("mag_hdgXY_deg"),"o",ms=1,color="tab:olive")
    ax3.plot(timeDataNew, fullData.get("mag_hdgXZ_deg"),"o",ms=1,color="tab:green")
    ax3.plot(timeDataNew, fullData.get("mag_hdgYZ_deg"),"o",ms=1,color="tab:purple")
    
    fig3, ax4 = plt.subplots()
    ax4.plot(timeDataNew, fullData.get("accelX_mG"),"o",ms=1,color="tab:olive")
    ax4.plot(timeDataNew, fullData.get("accelY_mG"),"o",ms=1,color="tab:green")
    ax4.plot(timeDataNew, fullData.get("accelZ_mG"),"o",ms=1,color="tab:purple")