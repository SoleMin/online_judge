# title : 네트워크
from itertools import permutations
def solution(n, computers):
    networks=dict()

    for item in computers:
        if item.count(1)==1:
            index=item.index(1)
            if index not in networks.keys():networks[index]=set()
        else:
            index=[]
            while sum(item)!= 0:
                index.append(item.index(1))
                item[item.index(1)]=0
            for i in list(permutations(index,2)):
                networks[i[0]] = networks[i[0]]|set([i[1]]) if i[0] in networks.keys() else set([i[1]])
    prev_network=[]
    while True:
        net_list=list(networks.keys())
        if prev_network==net_list: break
        prev_network=net_list
        for net in net_list:

            for target in net_list:
                if target in networks[net]:
                    networks[net]=networks[net].union(networks[target])
                    networks[net]=networks[net]-set([net])
            for del_item in networks[net]:
                net_list.pop(net_list.index(del_item))
                del networks[del_item]
    
    return len(networks)