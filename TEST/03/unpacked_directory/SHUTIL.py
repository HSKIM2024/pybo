#SHUTIL.py
import shutil
import os

# #파일복사
# shutil.copy("source.txt", "destination.txt")
#
# #디렉토리복사
# shutil.copytree("source_directory","destination_directory")
#
# #디렉토리삭제
# shutil.rmtree("remove_directory")
#
# #파일이동
# shutil.move("source.txt","destination_directory")

#디스크사용량 확인
total, used, free = shutil.disk_usage("/")
print("Total:",total,"Used:",used,"Free:",free)
#파일압축
shutil.make_archive("C:/LOCAL/SOURCE/DJANGO_CODE/projects/mysite/TEST/archive","zip","C:/LOCAL/SOURCE/DJANGO_CODE/projects/mysite/TEST")
# 파일 압축 해제
shutil.unpack_archive('archive.zip', "C:/LOCAL/SOURCE/DJANGO_CODE/projects/mysite/TEST/unpacked_directory")

