
import numpy as np
from pyuvdata import UVData
from astropy.time import Time
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from mwa_preprocess import preprocess

def preprocess(datafile, calfile, chunk_size=2, phase_zenith=False, clobber=False):
    """
    Preprocess MWA data for HERA lstbinner.

    Apply cal solution, and split into jd labeled chunks.
    """
    uvd = UVData()
    uvd.read_uvfits(datafile)

    npzcal = np.load(calfile)

    # apply calibration
    for blt, vis in enumerate(uvd.data_array):
        uvd.data_array[blt,:,:,0] /= (np.conj(npzcal[f"{uvd.ant_1_array[blt]}x"]) * npzcal[f"{uvd.ant_2_array[blt]}x"])
        uvd.data_array[blt,:,:,1] /= (np.conj(npzcal[f"{uvd.ant_1_array[blt]}y"]) * npzcal[f"{uvd.ant_2_array[blt]}y"])

    # phase to drift scan.
    if phase_zenith:
        uvd.unphase_to_drift()

    # split up chunks
    chunk_size = chunk_size
    tarray = np.unique(uvd.time_array)
    nchunks = int(np.ceil(uvd.Ntimes / chunk_size))
    tchunks = [tarray[i * chunk_size: (i + 1) * chunk_size] for i in range(nchunks)]
    # write out calibrated chunks in jd format.
    for tchunk in tchunks:
        uvd_chunk = uvd.select(times=tchunk, inplace=False)
        uvd_chunk.write_uvh5(f'zen.{tchunk[0]:.5f}.uvh5', clobber=clobber)

def download_gdrive(data_folder, cal_folder, gpstime):
    """
    Download data from google drive folder with specified GPS time.
    """
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    drive = GoogleDrive(gauth)

    file_list = drive.ListFile({'q': f"'{data_folder}' in parents and trashed=False and title contains '{gpstime}.uvfits'"}).GetList()
    for file in file_list:
        file.GetContentFile(file['title'])

    file_list = drive.ListFile({'q': f"'{cal_folder}' in parents and trashed=False and title contains '{gpstime}_cal.npz'"}).GetList()
    for file in file_list:
        file.GetContentFile(file['title'])
