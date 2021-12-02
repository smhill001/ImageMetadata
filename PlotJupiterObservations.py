# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 08:33:27 2021

PURPOSE: Plot datetime versus CM (I, II, III) of Jupiter observations. 
         (will be generalizable to all planetary observations eventually)


@author: Steven Hill
"""

def PlotJupiterObservations():
    import sys
    drive='f:'
    sys.path.append(drive+'\\Astronomy\Python Play')
    sys.path.append(drive+'\\Astronomy\Python Play\Util')
    sys.path.append(drive+'\\Astronomy\Python Play\SpectroPhotometry\Spectroscopy')
    sys.path.append(drive+'\\Astronomy\Python Play\SPLibraries')
    import ephem
    import os
    import numpy as np
    import ConfigFiles as CF
    from datetime import datetime
    import EWLibV006 as EWL
    import matplotlib.pyplot as pl



    observer = ephem.Observer()
    #Location from Google Maps at 483 S Oneida Way, Denver 80224
    observer.lon = ephem.degrees('-104.907985')
    observer.lat = ephem.degrees('39.708200')

    date_list=[]
    cam_list=[]
    path='F:/Astronomy/Projects/Planets/Jupiter/Imaging Data/'
    dateUTarray=os.listdir(path)
    for i in dateUTarray:
        if os.path.isdir(path+i):
            #print(i)
            sessionlist=os.listdir(path+i)
            for j in sessionlist:
                if "csv" in j:
                    if "Jupiter_VideoMetaData" in j:
                        #print j
                        metadata=CF.video_metadata_list(path+i+"/"+j)
                        metadata.load_records()
                        for k in range(0,metadata.nrecords-1):
                            #print metadata.VideoFile[k]
                            strdate=metadata.VideoFile[k][0:15]
                            #print strdate
                            date=datetime.strptime(strdate,"%Y-%m-%d-%H%M")
                            #print date
                            date_list.append(date)
                            cam_list.append('CMOS')
                elif "fit" in j:
                    if "Aligned" in j:
                        #print j
                        strdate=j[0:15]
                        #print strdate
                        date=datetime.strptime(strdate,"%Y-%m-%d-%H%M")
                        #print date
                        date_list.append(date)
                        cam_list.append('CCD')
                        
    date_list_datetime,elev_list,airmass_list,CMI_list,CMII_list,\
        Io_vis_list,Europa_vis_list, \
        Ganymede_vis_list,Callisto_vis_list= \
        EWL.JupiterEphemLists(date_list,observer)
    print len(date_list_datetime)
    fig=pl.figure(figsize=(6.0, 4.0), dpi=150, facecolor="white")

    print cam_list
    CMOS_indices = [k for k, x in enumerate(cam_list) if x == 'CMOS']
    CCD_indices = [k for k, x in enumerate(cam_list) if x == 'CCD']

    pl.subplot(1,1, 1)
    ax=pl.scatter(np.array(CMI_list)[CMOS_indices]*180./np.pi,np.array(date_list_datetime)[CMOS_indices],s=2.0,color='C0')                            
    pl.scatter(np.array(CMI_list)[CCD_indices]*180./np.pi,np.array(date_list_datetime)[CCD_indices],s=2.0,color='C1')                            

    perijoveTime=['2020-07-25-0625','2020-09-16-0220','2021-07-21-0814','2021-09-02-2242','2021-10-16-1713']
    periJdatetimelist=[]
    for pjt in  range (0,len(perijoveTime)):
        periJdatetimelist.append(datetime.strptime(perijoveTime[pjt],"%Y-%m-%d-%H%M"))
    juno_list_datetime,Juno_elev_list,Juno_airmass_list,Juno_CMI_list,Juno_CMII_list,\
        Juno_Io_vis_list,Juno_Europa_vis_list, \
        Juno_Ganymede_vis_list,Juno_Callisto_vis_list= \
        EWL.JupiterEphemLists(periJdatetimelist,observer)

    JunoCMIEqX=[277.3,216.4,107.,225.,132.]
    pl.scatter(JunoCMIEqX,periJdatetimelist,color='k',s=10)      
    pl.scatter(np.array(Juno_CMI_list)*180./np.pi,juno_list_datetime,color='r',s=10)      
    pl.xticks(fontsize=8)
    pl.xlim(0.0,360.0)
    pl.xticks(np.linspace(0.,360.,13, endpoint=True))
    pl.yticks(fontsize=8)
    pl.xlabel("CM I Longitude (deg)",fontsize=10)
    pl.grid(linewidth=0.2)
    pl.subplots_adjust(left=0.10, bottom=0.12, right=0.95, top=0.92)

