#!/bin/bash
cd /home/csv
/usr/local/bin/gts ID:PASSWORD ALL save_csv
cd /home
/usr/local/bin/python /home/gts_csv_dropbox_uploader.py