def increasing_array(n, nums):
    ans = 0
    for i in range(1, n):
        if nums[i] < nums[i - 1]:
            ans += nums[i - 1] - nums[i]
            nums[i] = nums[i - 1]
    return ans


if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))
    print(increasing_array(n, nums))
