# title : 주식가격
# not passed
def solution(prices):
    answer=[]
    for idx,i in enumerate(prices[:-1]):
        index=1
        if min(prices[idx+1:-1])>=i:
            answer.append(len(prices)-idx)
        else:
            for j in prices[idx+1:-1]:  
                if i<=j:
                    index+=1
                else:
                    break
            answer.append(index)
    answer.append(0)
    return answer