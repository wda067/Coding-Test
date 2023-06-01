# https://school.programmers.co.kr/learn/courses/30/lessons/42842
# level2

def solution(brown, yellow):
    total = brown + yellow
    for i in range(3, brown // 2):
        for j in range(3, brown // 2):
            if i >= j and total == i * j and (i - 2) * (j - 2) == yellow:
                return [i, j]

brown = 18
yellow = 6
print(solution(brown, yellow))
# 정답 : [8, 3]
