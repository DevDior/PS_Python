import sys

N = int(sys.stdin.readline())
nums = []

for _ in range(N):
    nums.append(int(sys.stdin.readline()))
    
def dividesort(list):
    if len(list) == 1:
        return list
    else:
        m = len(list)//2
        leftList = list[0:m]
        rightList = list[m:]
        
        leftList = dividesort(leftList)
        rightList = dividesort(rightList)
        
        answer = []
        
        cl = 0
        size_left = len(leftList)
        cr = 0
        size_right = len(rightList)
        
        while (cl != size_left) and (cr != size_right):
            if leftList[cl] <= rightList[cr]:
                answer.append(leftList[cl])
                cl += 1
            else:
                answer.append(rightList[cr])
                cr += 1
                
        if cl == size_left:
            for i in range(cr, size_right):
                answer.append(rightList[i])
        else:
            for i in range(cl, size_left):
                answer.append(leftList[i])
            
        return answer
        
answerList = dividesort(nums)

for j in answerList:
    print(j)