import argparse
from mwa_preprocess import preprocess

ap = argparse.ArgumentParser(description="Apply preprocessing to raw MWA observation to prepare it for HERA lstbinner")

ap.add_argument("datafile", type=str, help="name of input datafile. Must be .uvfits")
ap.add_argument("calfile", type=str, help="name of input .npz calibration file. Must be Wenyang .npz format.")
ap.add_argument("--chunk_size", type=int, default=2, help="split data into chunks with this length.")
ap.add_argument("--phase_zenith", default=False, action="store_true", help="rephase all data to zenith.")
ap.add_argument("--clobber", default=False, action="store_true", help="overwrite existing outputs.")

args = ap.parse_args()

preprocess.preprocess(args.datafile, args.calfile, args.chunk_size, args.phase_zenith, args.clobber)
