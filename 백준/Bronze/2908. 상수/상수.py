string = input()
rev_string = string[::-1]
a, b = map(int, rev_string.split())
print(max(a, b))
