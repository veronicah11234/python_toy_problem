def solution(A):
    N = len(A)

    total_bricks = sum(A)
    if total_bricks % N != 0:
        return -1

    target_per_box = total_bricks // N

    moves = 0

    for i in range(N):
        diff = A[i] - target_per_box

        if i < N - 1:
            A[i + 1] += diff
            moves += abs(diff)

    return moves

print(solution([7, 15, 10, 8])) 
print(solution([11, 10, 8, 12, 8, 10, 11])) 
print(solution([7, 14, 10]))  
