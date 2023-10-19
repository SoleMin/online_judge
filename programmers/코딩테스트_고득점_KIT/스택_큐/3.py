# title : 기능개발
from math import ceil
def solution(progresses, speeds):
    days=[min(ceil((100-progresses[0])/speeds[0]),1)]
    answer=[]
    for idx in range(1,len(progresses)):
        time=round((100-progresses[idx])/speeds[idx])
        if max(days)<time:
            answer.append(len(days))
            days=[time]
        else:
            days.append(time)
    answer.append(len(days)) 
    return answer