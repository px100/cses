if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        x, y = map(int, input().split())
        n = max(x, y)
        m = n * (n - 1) + 1
        if n % 2 == 0:
            print(m + x - y)
        else:
            print(m + y - x)
