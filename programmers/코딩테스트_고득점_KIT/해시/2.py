# title : 폰켓몬
def solution(nums):
    pon_set=set(nums)
    num_max=len(pon_set) if len(nums)//2>len(pon_set) else len(nums)//2
    return num_max