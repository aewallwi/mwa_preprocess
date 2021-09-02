# script that downloads observations from a google drive associated with a user specified jd.

import argparse
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


ap = argparse.ArgumentParser(description='google drive data downloader')
ap.add_argument('--folder', type=str, required=True, help="unique identifier for google drive folder containing observations. To find this, navigate to google drive folder and find string in url after '/folder/...'")
ap.add_argument('--jd', type=float, required=True, help="julian date of observation.")

gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

file_list = drive.ListFile({'q': f"'{ap.folder}' in parents and trashed=False and title contains '{jd}'"}).GetList()
for file in file_list:
    file.GetContentFile(file['title'])
