#! /usr/bin/env python

import os
from datetime import datetime, timedelta

seven_days = (datetime.now() - timedelta(days=7)).strftime("%d-%m-%y")

path = os.path.dirname(os.path.abspath(__file__))

dir = os.listdir(path)
for file in dir:
    if seven_days in file:
        file_name = os.path.join(path , file)
        os.remove(file_name)
