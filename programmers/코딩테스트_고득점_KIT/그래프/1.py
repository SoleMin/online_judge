# title : 가장 먼 노드
def solution(n, edge):
    visit=[None]*n
    visit[0]=0
    item=[set() for _ in range(n)]

    for i in edge:
        x,y=i[0]-1,i[1]-1
        item[x].add(y)
        item[y].add(x)
    waiting=set()
    waiting=waiting|item[0]
            
    depth=1
    new_waiting=waiting.copy()
    while None in visit:

        waiting=new_waiting.copy()
        new_waiting=set()
        for idx in waiting:
            if visit[idx] == None:
                visit[idx]=depth
                for item_idx in item[idx]:
                    if visit[item_idx] == None:
                        new_waiting.add(item_idx)
        depth+=1
    return visit.count(max(visit))