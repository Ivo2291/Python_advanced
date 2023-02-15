string = input().split("|")
sublists = []

for index in range(len(string) - 1, - 1, -1):
    sublists.extend(string[index].strip().split())

print(' '.join(sublists))
