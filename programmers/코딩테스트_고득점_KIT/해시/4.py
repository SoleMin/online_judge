# title : 의상
def solution(clothes):
    clothes_dict=dict()
    
    for i in clothes:
        if i[1] in clothes_dict.keys():
            clothes_dict[i[1]].append(i[0])
        else:
        
            clothes_dict[i[1]]=[i[0]]
    result=1
    for i in clothes_dict.keys():
        result*=len(clothes_dict[i])+1

    return result-1