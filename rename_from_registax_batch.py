#path="C:/Astronomy/Data/2024/10/27UT/"

def rename_from_registax_batch(path):
    import os
    fnlist = os.listdir(path)
    #print(fnlist)
    for fn in fnlist:
        if ".png" in fn:
        #if ".png" in fn and "BLU" in fn:
            print(fn)
            x=fn.split("2026")
            print(x[0],x[1])
            y=x[1].split(".")
            fnout="2026"+y[0]+"-"+x[0][0:-1]+".png"
            #fnout="2024"+y[0]+x[0][0:-1]+".png"
            print("fnout",fnout)
            os.rename(path+fn,path+fnout)