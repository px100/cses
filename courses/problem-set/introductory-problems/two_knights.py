if __name__ == "__main__":
    n = int(input())
    for i in range(1, n + 1):
        total = i * i * (i * i - 1) // 2
        attack = 4 * (i - 1) * (i - 2)
        print(total - attack)
