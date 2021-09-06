#!/usr/bin/env python

# script that downloads observations from a google drive associated with a user specified jd.

import argparse
from mwa_preprocess import preprocess


ap = argparse.ArgumentParser(description='google drive data uploader')
ap.add_argument('--data_folder', type=str, required=True, help="unique identifier for google drive folder containing observations. To find this, navigate to google drive folder and find string in url after '/folder/...'")
ap.add_argument('--data_files', type=str, required=True, nargs="+", help="List of datafiles to upload.'")
ap.add_argument("--sleep_time", type=float, default=0., help="time interval to wait between uploading each file.")
ap.add_argument("--retry_time", type=float, default=60., help="time interval to wait on a failure to connect before retrying. ")
#ap.add_argument('--mode', type=str, default='both', help="specify whether to download 'data', 'cal' or 'both'")

args = ap.parse_args()

preprocess.upload_gdrive(data_folder=args.data_folder, args.data_files,
                         sleep_time=args.sleep_time, retry_time=args.retry_time)
