# title : 베스트 엘범
def solution(genres, plays):
    genre_dict=dict()
    genre_count_dict=dict()
    for i in range(len(genres)):
        g=genres[i]
        c=plays[i]
        if g in genre_count_dict.keys():
            genre_count_dict[g]+=c
            genre_dict[g][i]=c
        else:
            genre_count_dict[g]=c
            genre_dict[g]=dict()
            genre_dict[g][i]=c
    sorted_genre_count_dictsorted={k: v for k, v in sorted(genre_count_dict.items(), key=lambda x:x[1],reverse=True)}
    answer=[]
    for i in sorted_genre_count_dictsorted:
        sorted_genre_dict={k: v for k, v in sorted(genre_dict[i].items(), key=lambda x:x[1],reverse=True)}
        
        answer+=list(sorted_genre_dict.keys())[:2]
    return answer