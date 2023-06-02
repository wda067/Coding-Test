# https://school.programmers.co.kr/learn/courses/30/lessons/1844
# level 2
# BFS 풀이

from collections import deque

def solution(maps):

    # 상:(-1, 0), 하:(1, 0), 좌:(0, -1), 우:(0, 1)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()  # 큐 객체 생성
    queue.append([0, 0])

    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()  # 현재 좌표

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 맵을 벗어날 때
            if (nx < 0 or nx >= len(maps)) or (ny < 0 or ny >= len(maps[0])):
                continue

            # 벽일 때
            if maps[nx][ny] == 0:
                continue

            # 처음 지나가는 길이면 거리 계산
            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))  # 재귀

    answer = maps[-1][-1]  # 최우측 하단 값 반환
    return -1 if answer == 1 else answer

maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
print(solution(maps))
