text = input()

characters = {}

for char in text:
    if char not in characters:
        characters[char] = 1
    else:
        characters[char] += 1

for key, value in sorted(characters.items()):
    print(f"{key}: {value} time/s")
