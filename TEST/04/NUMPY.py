#NUMPY.py
import numpy as np

#배열생성
arr = np.array([1,2,3,4,5])
print("배열:",arr)

#배열크기변경
reshaped_arr = arr.reshape((5,1))
print("변경된 배열형태:",reshaped_arr)

#배열연산
arr2 = np.array([6,7,8,9,10])
sum_arr = arr + arr2
print("배열 합 :",sum_arr)

#통계계산
mean_value = np.mean(arr)
print("평균값: ", mean_value)

max_value = np.max(arr)
print("최댓값: ", max_value)

min_value = np.min(arr)
print("최솟값: ", min_value)