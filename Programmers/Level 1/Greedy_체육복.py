# https://school.programmers.co.kr/learn/courses/30/lessons/42862
# level 1

def solution(n, lost, reserve):
    # reserve가 lost와 중복되면 안되기 때문에 중복 값은 제거
    set_reserve = set(reserve) - set(lost)
    set_lost = set(lost) - set(reserve)

    # for문의 순서때문에 reserve의 왼쪽부터 빌려준다
    for i in set_reserve:
        if i-1 in set_lost:
            set_lost.remove(i-1)
        elif i+1 in set_lost:
            set_lost.remove(i+1)
    return n-len(set_lost)


n = 5
lost = [2, 4]
reserve = [1, 3, 5]
print(solution(n, lost, reserve))
