#ARROW.py
import arrow

#현재시간 가져오기
now = arrow.now()
print("현재시간 : ", now)

#특정시간대의 현재시간가져오기
now_in_tokyo = arrow.now("Asia/Tokyo")
print("도쿄의 현재시간: ", now_in_tokyo)

#날짜파싱
date = arrow.get("2023-01-01","YYYY-MM-DD")
print("파싱된 날짜: ", date)

#날짜포맷팅
formatted_date = now.format("YYYY-MM-DD HH:mm:ss")
print("포맷된 날짜: ",formatted_date)

#날짜조작
tomorrow = now.shift(days=+1)
print("내일: ",tomorrow)


