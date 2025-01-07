def can_divide(n):
    total_sum = n * (n + 1) // 2
    if total_sum % 2 != 0:
        return False, None, None
    target = total_sum // 2
    set1, set2 = [], []
    for i in range(n, 0, -1):
        if i <= target:
            set1.append(i)
            target -= i
        else:
            set2.append(i)
    return True, set1, set2


if __name__ == "__main__":
    n = int(input())
    possible, set1, set2 = can_divide(n)
    if possible:
        print("YES")
        print(len(set1))
        print(" ".join(map(str, set1)))
        print(len(set2))
        print(" ".join(map(str, set2)))
    else:
        print("NO")
