# 리모컨
import sys
input = sys.stdin.readline

answer_list = []
now_num = '100'
answer_num = ''
N = input().strip()
N_count = len(N)
M = int(input())
enable_nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
broken_numbers = []

if M != 0:
    broken_numbers = list(input().split())

for i in broken_numbers:
    enable_nums[int(i)] = -1
max_num = max(enable_nums)
min_num = 0
for i in enable_nums:
    if i != -1:
        min_num = i
        break

# +, -만 조작한 횟수
if int(now_num) > int(N):
    answer_list.append(int(now_num) - int(N))
else:
    answer_list.append(int(N) - int(now_num))

# 숫자 조작 후 +, - 조작한 횟수
# 숫자 조작
if M != 10:
    answer = 0
    for i, n in enumerate(N):
        n = int(n)
        if enable_nums[n] != -1:
            answer_num += str(enable_nums[n])
            answer += 1
        else:
            _ = 0
            is_find = False
            while is_find == False:
                t_nums = [-1, -1]
                t_num = int(n) + _
                m_t_num = int(n) - _
                    
                if t_num >= 0 and t_num <= 10 and enable_nums[t_num] != -1:
                    t_nums[0] = t_num
                if m_t_num >= 0 and m_t_num <= 9 and enable_nums[m_t_num] != -1:
                    t_nums[1] = m_t_num
                
                if i != N_count -1 and int(N[i+1]) < 5:
                    tmp = t_nums[0]
                    t_nums[0] = t_nums[1]
                    t_nums[1] = tmp
                
                for e in t_nums:
                    if e != -1:
                        is_find = True
                        break
                _ += 1
            
            for j in t_nums:
                if j != -1:
                    answer_num += str(enable_nums[j])
                    if enable_nums[j] == 10:
                        answer += 2
                    else:
                        answer += 1
                    if answer_num == '0':
                        break
                        
                    if i != N_count-1:
                        ext_count = N_count -1 -i
                        if n > enable_nums[j]:
                            answer_num += str(max_num) * ext_count
                        else:
                            answer_num += str(min_num) * ext_count
                        answer += ext_count
                    break
            break
    # 숫자 조작 후, +, - 조작
    if answer_num != N:
        if int(answer_num) > int(N):
            answer += int(answer_num) - int(N)
        else:
            answer += int(N) - int(answer_num)
    answer_list.append(answer)

print(min(answer_list))