#GLOB.py
import glob

#현재 디렉토리에서 모든 .py 파일목록을 찾음
for filename in glob.glob("*.py"):
    print(filename)

#하위 디렉토리를 포함하여 .py 파일목록을 찾음
for filename in glob.glob(" **/*.py",recursive=True):
    print(filename)