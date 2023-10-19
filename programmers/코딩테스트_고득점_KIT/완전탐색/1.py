# title : 최소 직사각형
def solution(sizes):
    w_max=0
    h_max=0
    for i in sizes:
        if i[0]>i[1]:
            i[0],i[1]=i[1],i[0]
        if w_max<i[0]:w_max=i[0]
        if h_max<i[1]:h_max=i[1]
    return w_max*h_max
