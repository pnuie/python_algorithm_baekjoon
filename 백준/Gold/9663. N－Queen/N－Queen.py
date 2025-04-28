def checking(r, c):
    for j in range(len(check)):
        if abs(j - r) == abs(check[j] - c):
            return False
    return True


def dfs(r):
    global count
    global save
    if r == N:
        count += 1
        return

    for col in range(N):
        if col not in check:
            if checking(r, col):
                check.append(col)
                dfs(r + 1)
                check.pop()
            if check and N % 2 == 0:
                if check[0] == N / 2 :
                    print(count * 2)
                    exit()
            if check and not N % 2 == 0:
                if check[0] == N // 2 - 1 :
                    save = count
                if check[0] == N // 2 + 1:
                    print(count + save)
                    exit()


N = int(input())

check = []
count = 0

dfs(0)

print(count)