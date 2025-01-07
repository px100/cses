from itertools import combinations


def minimum_weight_diff(n, weights):
    total = sum(weights)
    half = n // 2

    left_sums = set()
    for r in range(half + 1):
        for combo in combinations(weights[:half], r):
            left_sums.add(sum(combo))

    right_sums = set()
    for r in range(n - half + 1):
        for combo in combinations(weights[half:], r):
            right_sums.add(sum(combo))

    min_diff = total
    for left_sum in left_sums:
        for right_sum in right_sums:
            group_sum = left_sum + right_sum
            diff = abs(total - 2 * group_sum)
            min_diff = min(min_diff, diff)

    return min_diff


if __name__ == "__main__":
    n = int(input())
    weights = list(map(int, input().split()))
    print(minimum_weight_diff(n, weights))
