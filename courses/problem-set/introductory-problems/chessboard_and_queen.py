def count_configs(board):
    n = 8
    reserved = [int(''.join('1' if c == '*' else '0' for c in row), 2) for row in board]
    count = 0

    def backtrack(r, c, d1, d2):
        nonlocal count
        if r == n:
            count += 1
            return
        free_pos = ~(c | d1 | d2 | reserved[r]) & ((1 << n) - 1)
        while free_pos:
            c_ = free_pos & -free_pos
            backtrack(r + 1, c | c_, (d1 | c_) << 1, (d2 | c_) >> 1)
            free_pos &= free_pos - 1

    backtrack(0, 0, 0, 0)
    return count


if __name__ == "__main__":
    board = [input().strip() for _ in range(8)]
    print(count_configs(board))
