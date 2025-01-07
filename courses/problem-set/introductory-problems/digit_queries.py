def find_digit_at_pos(k):
    i = 1
    while k > 9 * i * (10 ** (i - 1)):
        k -= 9 * i * (10 ** (i - 1))
        i += 1
    num = 10 ** (i - 1) + (k - 1) // i
    return str(num)[(k - 1) % i]


if __name__ == "__main__":
    q = int(input())
    for _ in range(q):
        k = int(input())
        print(find_digit_at_pos(k))
