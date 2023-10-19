# title : 같은 숫자는 싫어
def solution(arr):    
    answer = [arr[0]]
    for i in range(len(arr[1:])):
        if answer[-1] != arr[i]:
            answer.append(arr[i])

    return answer