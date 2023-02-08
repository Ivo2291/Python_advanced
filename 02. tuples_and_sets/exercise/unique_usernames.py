number_of_lines = int(input())
usernames = set()

for name in range(number_of_lines):
    username = input()
    usernames.add(username)

print(*usernames, sep="\n")
