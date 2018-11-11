import dropbox
import sys
import os
import ConfigParser

config = ConfigParser.ConfigParser()
config.readfp(open(r"config.ini"))
dropbox_token = config.get("Dropbox", "dropbox_token")
upload_to_folder = config.get("Dropbox", "upload_to_folder")
rootdirx = config.get("Dropbox", "rootdir_for_oswalk")

#dropbox
dbx = dropbox.Dropbox(dropbox_token)

for dir, dirs, files in os.walk(rootdirx):
    for file in files:
        try:
            file_path = os.path.join(dir, file)
            dest_path = os.path.join(upload_to_folder, file)
            with open(file_path) as f:
                dbx.files_upload(f.read(), dest_path, mute=True)
                print("Upload completed.")
        except Exception as err:
            print("Failed to upload.")

