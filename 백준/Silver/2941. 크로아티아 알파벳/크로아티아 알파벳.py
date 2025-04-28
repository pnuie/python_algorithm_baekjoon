word = input()
croatia = ['dz=', 'c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']
for x in croatia:
    word = word.replace(x, '0')

print(len(word))