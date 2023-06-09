# https://school.programmers.co.kr/learn/courses/30/lessons/42860
# level 2


def solution(name):
    from string import ascii_uppercase

    alphabet_list = list(ascii_uppercase)

    move = len(name) - 1
    sorted_name = ''.join(sorted(name))
    cnt = 0
    for i in range(len(name)):  # Up, Down 계산
        if sorted_name[i] != 'A':
            if alphabet_list.index(sorted_name[i]) <= 13:
                cnt += alphabet_list.index(sorted_name[i])
            else:
                cnt += sorted(alphabet_list, reverse=True).index(sorted_name[i]) + 1

        # 연속되는 A의 개수 확인
        next_idx = i + 1
        while next_idx < len(name) and name[next_idx] == 'A':
            next_idx += 1

        # Left, Right 계산
        move = min(move, i * 2 + len(name) - next_idx)  # 순서대로 가는 경우 vs 뒤로 돌아가는 경우
        move = min(move, (len(name) - next_idx) * 2 + i)  # 처음부터 뒤로 돌아가는 경우 고려

    return cnt + move

name = "AABBAAB"
print(solution(name))
