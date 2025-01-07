def find_missing_number(n, nums):
    return n * (n + 1) // 2 - sum(nums)


if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))
    print(find_missing_number(n, nums))
