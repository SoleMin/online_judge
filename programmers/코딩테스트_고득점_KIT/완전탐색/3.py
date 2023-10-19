# title : 소수 찾기
from itertools import permutations
def is_prime(x):
    import math
    if x<2: return False
    for i in range(2,int(math.sqrt(x))+1):
        if x%i==0: return False
    return True

def solution(numbers):
    answer = 0
    numbers=list(numbers)
    permut_arr=[]
    for idx in range(1,len(numbers)+1):
        for i in list(permutations(numbers,idx)):
            permut_arr.append(int(''.join(i)))

    for i in set(permut_arr):

        if is_prime(i):
            answer+=1
    
    return answer