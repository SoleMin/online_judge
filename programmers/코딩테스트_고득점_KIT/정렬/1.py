# title : K번째 수
def solution(array, commands):
    answer=[]
    for i in commands:
        a=array[i[0]-1:i[1]]
        a=sorted(a)
        answer.append(a[i[2]-1])
    return answer