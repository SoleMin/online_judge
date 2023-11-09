# title : 주식가격
# not passed (change DFS -> BFS)

def solution(maps):
    target_location=(len(maps)-1,len(maps[0])-1)
    queue=[]
    queue.append([(0,0),maps.copy(),1])
    min_step=-1
    while queue:
        cur_location,memory,step=queue.pop()
        if target_location==cur_location:
            if min_step < 0 or min_step > step:
                min_step=step
        elif min_step > 0 and step > min_step:
            pass
        else:
            x=cur_location[0]
            y=cur_location[1]

            memory[x][y]=0 # visited
            if x+1 <len(memory) and memory[x+1][y]==1:      #down
                queue.append([(x+1,y),memory.copy(),step+1])
            if x > 0 and memory[x-1][y]==1:                 #up
                queue.append([(x-1,y),memory.copy(),step+1])
            if y+1 < len(memory[0]) and memory[x][y+1]==1:  #left
                queue.append([(x,y+1),memory.copy(),step+1])
            if y > 0 and memory[x][y-1]==1:                 #right
                queue.append([(x,y-1),memory.copy(),step+1])
    return min_step