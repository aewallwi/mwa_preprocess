import numpy as np
from pyuvdata import UVData
import argparse
from astropy.time import Time

ap = argparse.ArgumentParser(description="Apply preprocessing to raw MWA observation to prepare it for HERA lstbinner")

ap.add_argument("datafile", type=str, help="name of input datafile. Must be .uvfits")
ap.add_argument("calfile", type=str, help="name of input .npz calibration file. Must be Wenyang .npz format.")
ap.add_argument("--chunk_size", type=int, default=2, help="split data into chunks with this length.")
ap.add_argument("--phase_zenith", default=False, action="store_true", help="rephase all data to zenith.")
ap.add_argument("--clobber", default=False, action="store_true", help="overwrite existing outputs.")

args = ap.parse_args()

uvd = UVData()
uvd.read_uvfits(args.datafile)

npzcal = np.loadz(args.calfile)

# apply calibration
for blt, vis in enumerate(uvd.data_array):
    uvd.data_array[blt,:,:,0] /= (np.conj(npzcal[f"{uvd.ant_1_array[blt]}x"]) * npzcal[f"{uvd.ant_2_array[blt]}x"])
    uvd.data_array[blt,:,:,1] /= (np.conj(npzcal[f"{uvd.ant_1_array[blt]}y"]) * npzcal[f"{uvd.ant_2_array[blt]}y"])

# phase to drift scan.
if args.phase_zenith:
    uvd.unphase_to_drift()

# split up chunks
chunk_size = args.chunk_size
tarray = np.unique(uvd.time_array)
nchunks = int(np.ceil(uvd.Ntimes / chunk_size))
tchunks = [tarray[i * chunk_size: (i + 1) * chunk_size] for i in range(nchunks)]
# write out calibrated chunks in jd format.
for tchunk in tchunks:
    uvd_chunk = uvd.select(times=tchunk, inplace=False)
    uvd_chunk.write_uvh5(f'zen.{tchunk[0]:.5f}.uvh5', clobber=args.clobber)
