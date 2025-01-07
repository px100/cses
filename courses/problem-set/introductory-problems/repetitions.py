def max_length_substring(s):
    ans = 1
    count = 1
    for i in range(1, len(s)):
        count = count + 1 if s[i] == s[i - 1] else 1
        ans = max(ans, count)
    return ans


if __name__ == "__main__":
    s = input()
    print(max_length_substring(s))
