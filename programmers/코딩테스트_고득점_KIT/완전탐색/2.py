# title : 모의고사
from math import ceil
def solution(answers):
    answer = []
    a=[1, 2, 3, 4, 5]
    b=[2, 1, 2, 3, 2, 4, 2, 5]
    c=[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    prob_len=len(answers)
    arr=[]
    for i in [a,b,c]:
        arr.append((i*(max(1,ceil(prob_len/len(i)))))[:len(answers)])
    result=[]
    for i in arr:
        result.append(sum([p== a for p,a in zip(answers, i)]))
    for idx,i in enumerate(result):
        if i == max(result):
            answer.append(idx+1)
    return answer