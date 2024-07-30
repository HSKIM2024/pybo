#PATHLIB.py
from pathlib import Path

#경로객체생성
p = Path("/LOCAL/SOURCE/DJANGO_CODE/projects/mysite")
#하위경로생성 및 파일경로조합
new_path = p / "db.sqlite3"
print(new_path)

#파일 및 디렉토리 존재여부확인
if new_path.exists():
    print("File exists")
else:
    print("File does not exist")

#디렉토리 순회
for file in p.glob("*.py"):
    print(file)

#파일 읽기 및 쓰기
path_to_file = Path("example.txt")
path_to_file.write_text("Hello, pathlib!")
print(path_to_file.read_text())

#경로정보추출
print("File name:",path_to_file.name)
print("File extension:",path_to_file.suffix)
print("Parent directory",path_to_file.parent)
