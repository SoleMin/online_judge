# title : 프로세스
def solution(priorities, location):
    
    process_num =list(range(len(priorities)))
    turn=0
    while(True):
        priority=max(priorities)
        item,priorities=priorities[0],priorities[1:]
        process_item,process_num=process_num [0],process_num[1:]
        if priority<=item:
            turn +=1
            if process_item==location:
                return turn 
        else:
            priorities.append(item)
            process_num.append(process_item)
