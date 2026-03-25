# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 12:09:48 2018

@author: Steven Hill
"""
import sys
drive='c:'
sys.path.append(drive+'/Astronomy/Python Play')
sys.path.append(drive+'/Astronomy/Python Play/Util_P3')
sys.path.append(drive+'/Astronomy/Python Play/SpectroPhotometry/Spectroscopy')
sys.path.append(drive+'/Astronomy/Python Play/TechniquesLibrary')

import ConfigFiles as CF
#import FITSSpecUtils as FSU
#import SysRespLIB as SRL
#import GeneralSpecUtils as GSU
import numpy as np
#import matplotlib.pyplot as pl
#import scipy, datetime, time
#import MetaUtils as MU
 
#from os import listdir
    
    
class MetaDatafromFile(CF.readtextfilelines):
    """
    This class builds on the readtextfilelines class to add parameters 
    for setting up plots. It will also do the initial plot setup.
    
    SMH 6/7/18
    """
    pass
    def loadmetadata(self):
        #import numpy as np
        #View has two options: raw or flux?
        self.KeyList=["Binning","Capture Area","Gain","Exposure","Gamma","TimeStamp"]
        preferredorder=[5,3,2,4,0,1]
        self.KeyList = [ self.KeyList[i] for i in preferredorder]
        print(self.KeyList)
        self.TempList=[]
        for recordindex in range(1,self.nrecords):
            fields=self.CfgLines[recordindex].split('=')
            #print fields
            #print self.TempList
            #TempList.append(recordindex)
            if "Binning" in fields[0]:
                self.TempList.append(int(fields[1]))
            if "Capture Area" in fields[0]:
                temp=str(fields[1])
                self.TempList.append(temp.replace("\n",""))
            if "Gain" in fields[0]:
                if "Auto Exp Max" not in fields[0] and "Exposure" not in fields[0]:
                    self.TempList.append(float(fields[1]))               
                    
            if "Exposure" in fields[0]:
                if "Gain" not in fields[0]:
                    if "s" in fields[1]: #Handle seconds and milliseconds
                        if "ms" in fields[1]: #Handle milliseconds
                            self.TempList.append(float(fields[1][:-3])/1000.)
                        else: #Handle seconds
                            self.TempList.append(float(fields[1][:-2]))
                    else: #Handle time for SharpCap versions <4.0
                        self.TempList.append(float(fields[1]))
                    
            if "Gamma" in fields[0]:
                if "Display" not in fields[0]:
                    self.TempList.append(float(fields[1]))
            if "Xpress" in fields[0]:
                print("HERE Sharpcap 4.1")
                self.TempList.append("No Gamma")
                
            if "TimeStamp" in fields[0]:
                if "Frames" not in fields[0]:
                    temp=str(fields[1])
                    self.TempList.append(temp.replace("\n",""))
        print()
        print(self.TempList)
                
        self.TempList = [ self.TempList[i] for i in preferredorder]
        print(self.TempList)
        print()
                    
                    