#FAKER.py
from faker import Faker

#Faker 객체생성, 원하는 로케일설정가능 (예: ko_KR은 한국어)
fake = Faker("ko_KR")

#가짜이름생성
print(fake.name())

#가짜주소생성
print(fake.address())

#가짜이메일생성
print(fake.email())

#가짜문장생성
print(fake.catch_phrase())


