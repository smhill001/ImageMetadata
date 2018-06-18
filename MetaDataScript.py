# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 06:41:33 2018

@author: Steven Hill
"""
def MakeMetaDataFile(Date,Target):
    import sys
    drive='f:'
    sys.path.append(drive+'\\Astronomy\Python Play')
    sys.path.append(drive+'\\Astronomy\Python Play\Util')
    sys.path.append(drive+'\\Astronomy\Python Play\SpectroPhotometry\Spectroscopy')
    sys.path.append(drive+'\\Astronomy\Python Play\TechniquesLibrary')
    
    import numpy as np
    import MetaUtils as MU    
    from os import listdir
    
    path="C:/Users/Steven Hill/Desktop/SharpCap Captures/"
    filelist=listdir(path)
    
    metadatafiles=[]
    videodatafiles=[]
    metadatalist=[]
    for fn in filelist:
        if Date in fn:
            if Target in fn:
                if "txt" in fn:
                    metadatafiles.append(fn)
                    #print path+fn
                    md=MU.MetaDatafromFile(path+fn)          
                    md.loadmetadata()
                    metadatalist.append(md.TempList)
                if "avi" in fn:
                    videodatafiles.append(fn)
            
    print len(metadatafiles)
    print len(videodatafiles)
    dbrecordlist=[]
    dbrecord=[]
    
    text_file = open(path+Date+"_"+Target+"_VideoMetaData.csv", "w")
    BigKeyList=["Video File","Meta File"]+ md.KeyList
    for item in BigKeyList:
        text_file.write("%s," % item)
    text_file.write("\n")
    
    for i in np.arange(0,len(metadatafiles)):
        dbrecord.append(videodatafiles[i])
        dbrecord.append(metadatafiles[i])
        dbrecord=dbrecord+metadatalist[i]
        for item in dbrecord:
            text_file.write("%s," % item)
        text_file.write("\n")
    
        dbrecordlist.append(dbrecord)
        dbrecord=[]
    text_file.close()   
    print dbrecordlist
    
        #print metadatafiles[i],videodatafiles[i],metadatalist[i]
