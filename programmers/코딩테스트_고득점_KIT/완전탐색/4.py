# title : 카펫
def solution(brown, yellow):
    w,h=3,2
    while True:
        if (w-2)*(h-2)==yellow and w*h-yellow==brown:return [w,h]
        h+=1
        w=h
        while (w-2)*(h-2)<yellow:
            w+=1
        
