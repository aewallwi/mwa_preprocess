from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()           
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

gauth = GoogleAuth()           
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)
file_list = drive.ListFile({'q': "'19KTJjXlZTz_o4lKpgyzp21Ae13Xupw_b' in parents and trashed=False and title contains '.metafits'"}).GetList()


for file in file_list:
    file.GetContentFile(file['title'])

import re
import numpy as np

gpstimes = [int(file['title'].split('.')[0]) for file in file_list]


import os
import shutil
import glob
from astropy.time import Time

t = Time(gpstimes, format='gps')
unique_jds = np.unique(t.jd.astype(int))
jds = t.jd

for jd, file in zip(jds.astype(int), file_list):
    if not os.path.isdir(f'{jd}'):
        os.mkdir(f'{jd}')
    shutil.move(file['title'], f'./{jd}/')


for jd in glob.glob('245*'):
    jdint = int(jd)
    flistjd = glob.glob(f'{jd}/*.metafits')
    gpstimes = [int(fn.split('/')[1].split('.')[0]) for fn in flistjd]
    t = Time(gpstimes, format='gps')
    jds = t.jd
    assert np.all(jds.astype(int) == jdint)
        
    
