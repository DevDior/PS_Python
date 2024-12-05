# 세탁소 사장 동혁
import sys

input = sys.stdin.readline

quarter = 25
dime = 10
nickel = 5
penny = 1

T = int(input())

for _ in range(T):
    change = int(input())
    
    quarter_count = change // quarter
    print(quarter_count, end=' ')
    change %= quarter
    
    dime_count = change // dime
    print(dime_count, end=' ')
    change %= dime
    
    nickel_count = change // nickel
    print(nickel_count, end=' ')
    change %= nickel
    
    penny_count = change // penny
    print(penny_count)