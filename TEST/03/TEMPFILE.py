#TEMPFILE.py
import tempfile

#임시파일 생성 및 사용
with tempfile.TemporaryFile(mode="w+t") as tmp:
    tmp.write("Hello, World!")
    tmp.seek(0)
    print(tmp.read())

#임시디렉토리 생성 및 사용
with tempfile.TemporaryDirectory() as tmpdirname:
    print("임시 디렉토리 경로: ", tmpdirname)
    #임시 디렉토리 내에서 파일생성 및 작업수행
