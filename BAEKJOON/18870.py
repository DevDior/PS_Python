# 좌표 압축
import sys

N = int(sys.stdin.readline())
coordinates_list = list(map(int, sys.stdin.readline().split()))
not_duplicated_list = list(set(coordinates_list))
not_duplicated_list.sort()
coordinates_dict = dict()

for i in range(len(not_duplicated_list)):
    coordinates_dict[not_duplicated_list[i]] = i
    
for j in coordinates_list:
    print(coordinates_dict[j], end=' ')