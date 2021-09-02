# script that downloads observations from a google drive associated with a user specified jd.

import argparse
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


ap = argparse.ArgumentParser(description='google drive data downloader')
ap.add_argument('--folder', type=str, required=True, help="unique identifier for google drive folder containing observations. To find this, navigate to google drive folder and find string in url after '/folder/...'")
ap.add_argument('--gpstime', type=float, required=True, help="gpstime of observation.")
ap.add_argument('--mode', type=str, default='both', help="specify whether to download 'data', 'cal' or 'both'")

args = ap.parse_args()

gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

if args.mode == 'both':
    file_list = drive.ListFile({'q': f"'{args.folder}' in parents and trashed=False and title contains '{args.gpstime}'"}).GetList()
elif args.mode == 'cal':
    file_list = drive.ListFile({'q': f"'{args.folder}' in parents and trashed=False and title contains '{args.gpstime}_cal.npz'"}).GetList()
elif args.mode == 'data':
    file_list = drive.ListFile({'q': f"'{args.folder}' in parents and trashed=False and title contains '{args.gpstime}.uvfits'"}).GetList()

for file in file_list:
    file.GetContentFile(file['title'])
