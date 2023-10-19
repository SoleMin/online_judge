# title : 피로도
def solution(k, dungeons):
    queue=[]
    queue.append([k,dungeons,0])
    min_val=0
    while queue:
        limit,item,depth=queue.pop(0)
        if len(item)==0:
            return depth
        for i in range(len(item)):
            if limit < item[i][0]:
                min_val=max(min_val,depth)
            else:
                new_item=item.copy()
                new_item.pop(i)
                queue.append([limit-item[i][1],new_item,depth+1])
    return min_val