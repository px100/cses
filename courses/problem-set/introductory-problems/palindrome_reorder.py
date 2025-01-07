from collections import Counter

if __name__ == "__main__":
    s = input()
    n = len(s)
    freq = Counter(s)
    odd_count = 0
    odd_char = ""
    for k, v in freq.items():
        if v % 2 == 1:
            odd_count += 1
            odd_char = k
    if odd_count > 1:
        print("NO SOLUTION")
    else:
        ans = ""
        for k, v in freq.items():
            ans += k * (v // 2)
        print(ans + odd_char + ans[::-1])
