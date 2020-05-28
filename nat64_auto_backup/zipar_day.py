#! /usr/bin/env python

import os, zipfile
from datetime import datetime, timedelta

yesterday = (datetime.now() - timedelta(days=1)).strftime("%d-%m-%y")

path = os.path.dirname(os.path.abspath(__file__))

file_zip = zipfile.ZipFile( yesterday + '.zip', 'w')

dir = os.listdir(path)
for file in dir:
    if yesterday in file:
        file_name = os.path.join(path , file)
        if file.endswith('.txt'):
            file_zip.write(os.path.relpath(os.path.join(file_name)), compress_type = zipfile.ZIP_DEFLATED)
            os.remove(file_name)

file_zip.close()
