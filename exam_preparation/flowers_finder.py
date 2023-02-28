from collections import deque

vowels = deque(input().split())
consonants = input().split()

flowers_dict = {"rose": "rose",
                "tulip": "tulip",
                "lotus": "lotus",
                "daffodil": "daffodil"}

word = ""

while vowels and consonants:

    vowel = vowels.popleft()
    consonant = consonants.pop()
    word_found = False

    for key, value in flowers_dict.items():

        if vowel in value:
            value = value.replace(vowel, '')

        if consonant in value:
            value = value.replace(consonant, '')

        flowers_dict[key] = value

        if not flowers_dict[key]:
            word = key
            word_found = True
            break

    if word_found:
        break

if word:
    print(f"Word found: {word}")
else:
    print("Cannot find any word!")

if vowels:
    print(f"Vowels left: {' '.join(vowels)}")

if consonants:
    print(f"Consonants left: {' '.join(consonants)}")
