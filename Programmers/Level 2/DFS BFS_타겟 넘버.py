# https://school.programmers.co.kr/learn/courses/30/lessons/43165
# level 2
# BFS 풀이

def solution(numbers, target):
    leaves = [0]  # 모든 계산 결과
    cnt = 0

    for num in numbers:
        temp = []

        # 자식 노드
        for leaf in leaves:
            temp.append(leaf + num)
            temp.append(leaf - num)

        leaves = temp

    # target과 같은 경우 카운트
    for leaf in leaves:
        if leaf == target:
            cnt += 1

    return cnt


numbers = [4, 1, 2, 1]
target = 4
print(solution(numbers, target))
