# title : 타겟 넘버
def backtrack(arr,numbers,target):
    if len(arr)==len(numbers):
        if sum(arr)==target:
            return 1
        return 0
        
    return backtrack(arr+[-numbers[len(arr)-1]],numbers,target)+backtrack(arr+[numbers[len(arr)-1]],numbers,target)
def solution(numbers, target):
    
    return backtrack([],numbers,target)