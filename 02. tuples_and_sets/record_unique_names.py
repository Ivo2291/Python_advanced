number = int(input())
unique_names = set()

for name in range(number):
    unique_names.add(input())

for name in unique_names:
    print(name)
