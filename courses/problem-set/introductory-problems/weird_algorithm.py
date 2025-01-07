def collatz_sequence(n):
    result = []
    while n != 1:
        result.append(n)
        n = n // 2 if n % 2 == 0 else 3 * n + 1
    result.append(1)
    return result


if __name__ == "__main__":
    n = int(input())
    sequence = collatz_sequence(n)
    print(' '.join(map(str, sequence)))
