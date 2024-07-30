#PYTZ.py
import pytz
from datetime import datetime

#현재시간 가져오기(UTC기준)
utc_now = datetime.utcnow()
print(f"현재 UTC시간 : {utc_now}")

#뉴욕 시간대로 변환
new_york_tz = pytz.timezone("America/New_York")
new_york_time = utc_now.replace(tzinfo=pytz.utc).astimezone(new_york_tz)
print(f"뉴욕시간 : {new_york_time}")

#서울 시간대로 변환
seoul_tz = pytz.timezone("Asia/Seoul")
seoul_time = utc_now.replace(tzinfo= seoul_tz).astimezone(seoul_tz)
print(f"서울시간 : {seoul_time}")
