import dbf
import os
import pandas as pd
import numpy as np
import rasterio as rs

paramtables = ["../data/cov/static/Soils/DrainageClass.dbf"]
MUCraster = "../data/cov/static/MapunitRaster_CONUS_90m1.tif"

outDir = "../data/cov/static/Soils/work"

#Convert dbfs to csvs
for paramtable in paramtables:


    paramName = os.path.splitext(os.path.basename(paramtable))[0]
    

    csvName = os.path.join(outDir, paramName + ".csv") #Create csv file
    print(csvName)

    db = dbf.Table(paramtable)
    db.open()

    dbf.export(db, csvName, header = True)

    df = pd.read_csv(csvName)


    d = pd.concat(df['mukey'], df['drnclass_1'])
    print(d)

    with rs.open(MUCraster) as ds: # load map unit code raster
        #MUC = ds.read(1)
        MUCNoData = ds.nodata # pull the no data value
        profile = ds.profile


        print(ds.profile)
        #print(len(np.unique(MUC)))


