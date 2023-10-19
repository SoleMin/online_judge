# title : 전략망을 둘로 나누기
def solution(n, wires):
    min_val=float('inf')
    for cut_idx in range(len(wires)):
        cuted_wires=wires.copy()
        cut_item=cuted_wires.pop(cut_idx)

        left,right=set([cut_item[0]]),set([cut_item[1]])
        queue=[i for i in cuted_wires]
        
        while queue:

            item=queue.pop(0)
            if item[0] in left or item[1] in left: left=left|set(item)
            elif item[0] in right or item[1] in right: right=right|set(item)
            else:queue.append(item)
        diff=abs(len(left)-len(right))
 
        if diff==0:
            return 0
        else:min_val=min(diff,min_val)
    return min_val