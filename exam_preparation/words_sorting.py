def words_sorting(*words):
    words_dict = {}
    result = 0
    output = ""

    for word in words:
        words_dict[word] = sum([ord(char) for char in word])

    for key, value in words_dict.items():
        result += value

    if result % 2 == 0:
        output += '\n'.join([f"{key} - {value}" for key, value in sorted(words_dict.items())])

    else:
        output += '\n'.join([f"{key} - {value}"
                             for key, value in sorted(words_dict.items(), key=lambda x: x[1], reverse=True)])

    return output


print(
    words_sorting(
        'escape',
        'charm',
        'eye'
    ))
