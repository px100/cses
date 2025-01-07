def generate_unique_permutations(s):
    def backtrack(path, used):
        if len(path) == len(s):
            result.append(''.join(path))
            return
        for i, char in enumerate(s):
            if used[i] or (i > 0 and s[i] == s[i - 1] and not used[i - 1]):
                continue
            used[i] = True
            backtrack(path + [char], used)
            used[i] = False

    s = sorted(s)
    result = []
    backtrack([], [False] * len(s))
    return result


if __name__ == "__main__":
    s = input()
    unique_perms = generate_unique_permutations(s)
    print(len(unique_perms), *unique_perms, sep='\n')
