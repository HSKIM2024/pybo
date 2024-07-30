#OS.py
import os

#현재 작업디렉토리 조회
current_directory = os.getcwd()
print("Current directory: ", current_directory)

#새 디렉토리 생성
os.mkdir("new_directory")

#디렉토리 삭제
os.rmdir("new_directory")

#환경변수 조회
path = os.environ.get("PATH")
print("PATH Environment Variable: ",path)

#더미파일을 생성하고 내용을 쓰기모드로 열기
with open("dummy.txt","w") as dummy_file:
    dummy_file.write("This is a dummy file.")

#파일이름변경
os.rename("dummy.txt","new_dummy.txt")

#파일삭제
os.remove("new_dummy.txt")

#시스템 명령 실행
os.system("echo Hello World")