def count_trailing_zeros(n):
    count = 0
    while n > 0:
        n //= 5
        count += n
    return count


if __name__ == "__main__":
    n = int(input())
    print(count_trailing_zeros(n))
