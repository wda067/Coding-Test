# https://www.acmicpc.net/problem/9012
# 실버 4

# Stack 문제

import sys

input = sys.stdin.readline
T = int(input())

for _ in range(T):
    stack = []
    vps = input().rstrip()
    isVPS = True

    for ch in vps:
        if ch == '(':  # ( 일 경우 스택에 push
            stack.append(ch)
        elif ch == ')':  # ) 이고 스택이 비어 있지 않은 경우 스택에서 pop
            if not stack:  # 스택이 비어 있을 경우
                isVPS = False
                break
            stack.pop()

    if not stack and isVPS:
        print('YES')
    elif stack or not isVPS:
        print("NO")
