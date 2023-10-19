# title : 체육복
def solution(n, lost, reserve):

    reserve_set=set(reserve)-set(lost)
    lost=list(set(lost)-set(reserve))
    answer=0
    for i in range(1,n+1):
        if i not in lost:
            answer+=1
        else:
            for a in [i-1,i+1]:
                if a in reserve_set:
                    answer+=1
                    reserve_set-=set([a])
                    break
    return answer