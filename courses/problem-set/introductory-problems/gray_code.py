if __name__ == "__main__":
    n = int(input())
    limit = 1 << n
    for i in range(limit):
        gray = i ^ (i >> 1)
        print(f"{gray:0{n}b}")
