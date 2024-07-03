# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 14:53:37 2024

@author: bloss
"""

import glob
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



if __name__ == "__main__":
    
    dataFile = pd.read_csv('/Users/bloss/OneDrive/documents/DataSets/ResistanceData-2024-7-03_SlipringTest1.csv')

    dataTime = dataFile.get("Time")/1000/1000/60

    plt.plot(dataTime, dataFile.get(" Res 2"))
    plt.plot(dataTime, dataFile.get(" Res 4"))
    plt.plot(dataTime, dataFile.get(" Res 6"))
    plt.title("Slipring Test 1 (-20C)")
    plt.xlabel("Time [min]")
    plt.ylabel("Resistance [ohms]")
    plt.legend(["Res 1","Res 2","Res 3"])
    plt.text(45, 90, 'Not rotating last 20 min', fontsize = 10)
    plt.grid()
    plt.show()