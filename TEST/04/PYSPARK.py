#PYSPARK.py
from pyspark.sql import SparkSession

#Spark 세션시작
spark = SparkSession.builder.appName('PySparkExample').getOrCreate()

#데이터프레임 생성
data = [("James","Smith","USA",30),
        ("Michael","Rose","USA",45),
        ("Robert","Williams","USA",15),
        ("Maria","Jones","USA",25)]

columns = ["Firstname","Lastname","Country","Age"]
df = spark.createDataFrame(data, schema = columns)

#데이터프레임 출력
df.show()

#Spark 세션 종료
spark.stop()