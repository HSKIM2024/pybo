#ZONEINFO.py
from datetime import datetime
from zoneinfo import ZoneInfo

# 현재 시간 가져오기 (UTC 기준)
utc_now = datetime.utcnow()
print(f"현재 UTC 시간:  {utc_now}")

# 뉴욕 시간대로 변환
new_york_time = utc_now.replace(tzinfo=ZoneInfo('America/New_York'))
print(f"뉴욕 시간: {new_york_time}")

# 서울 시간대로 변환
seoul_time = utc_now.replace(tzinfo=ZoneInfo('Asia/Seoul'))
print(f"서울 시간: {seoul_time}")