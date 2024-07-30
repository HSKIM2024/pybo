#DATEUTIL.py
from dateutil import parser

date_string = "2023-04-01 12:34:56"
date_obj = parser.parse(date_string)

print(date_obj)