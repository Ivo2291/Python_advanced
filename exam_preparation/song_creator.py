def add_songs(*args):
    songs = {}
    output_list = []

    for song in args:
        title = song[0]
        lyrics = song[1]

        if title not in songs:
            songs[title] = []
        songs[title].extend(lyrics)

    for key, value in songs.items():
        output_list.append("- " + key)
        output_list.extend(value)

    return '\n'.join(output_list)


print(add_songs(
    ("Beat It", []),
    ("Beat It",
     ["Just beat it (beat it), beat it (beat it)",
      "No one wants to be defeated"]),
    ("Beat It", []),
    ("Beat It",
     ["Showin' how funky and strong is your fight",
      "It doesn't matter who's wrong or right"]),
))
