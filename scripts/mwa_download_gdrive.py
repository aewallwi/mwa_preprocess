# script that downloads observations from a google drive associated with a user specified jd.

import argparse
from mwa_preprocess import preprocess


ap = argparse.ArgumentParser(description='google drive data downloader')
ap.add_argument('--data_folder', type=str, required=True, help="unique identifier for google drive folder containing observations. To find this, navigate to google drive folder and find string in url after '/folder/...'")
ap.add_argument('--cal_folder', type=str, required=True, help="unique identifier for google drive folder containing cal solutions. To find this, navigate to google drive folder and find string in url after '/folder/...'")
ap.add_argument('--gpstime', type=float, required=True, help="gpstime of observation.")
#ap.add_argument('--mode', type=str, default='both', help="specify whether to download 'data', 'cal' or 'both'")

args = ap.parse_args()

preprocess.download_gdrive(data_folder=args.data_folder, cal_folder=args.cal_folder,
                           gpstime=args.gpstime)
