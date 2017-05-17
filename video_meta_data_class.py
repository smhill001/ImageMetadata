# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 11:24:43 2017

@author: Astronomy
"""

class video_meta_data:
    # Reads the metadata from a single videa metadata file
    def __init__(self,VideoMetaDataFile):

        self.DateObs=''
        self.Target=''
        self.Camera=''
        self.Pan=0
        self.Tilt=0
        self.Output_Format=''
        self.Binning=0
        self.Capture_Area=''
        self.ColourSpace=''
        self.Sensor_Temp=0.
        self.Discard_Split_Frames=''
        self.High_Speed_Mode=''
        self.Turbo_USB=0
        self.Flip_Image=''
        self.Frame_Rate_Limit=''
        self.Gain=0
        self.Exposure=0.
        self.Timestamp_Frames=''
        self.Brightness=0
        self.Gamma=0
        self.AutoExpMaxGain=0
        self.AutoExpMaxExp=0
        self.AutoExpMaxBrightness=0
        self.Subtract_Dark=''
        self.Display_Brightness=0
        self.Display_Contrast=0
        self.Display_Gamma=0
        
        CfgFile=open(VideoMetaDataFile,'r')
        CfgLines=CfgFile.readlines()
        CfgFile.close()
        nrecords=len(CfgLines)
        #print CfgLines

        for recordindex in range(1,nrecords):
            fields=CfgLinesrecordindex.split(',')
            self.DateObs=VideoMetaDataFile0:16
            self.Target=''
            self.Camera=''
            self.Pan=0
            self.Tilt=0
            self.Output_Format=''
            self.Binning=0
            self.Capture_Area=''
            self.ColourSpace=''
            self.Sensor_Temp=0.
            self.Discard_Split_Frames=''
            self.High_Speed_Mode=''
            self.Turbo_USB=0
            self.Flip_Image=''
            self.Frame_Rate_Limit=''
            self.Gain=0
            self.Exposure=0.
            self.Timestamp_Frames=''
            self.Brightness=0
            self.Gamma=0
            self.AutoExpMaxGain=0
            self.AutoExpMaxExp=0
            self.AutoExpMaxBrightness=0
            self.Subtract_Dark=''
            self.Display_Brightness=0
            self.Display_Contrast=0
            self.Display_Gamma=0

