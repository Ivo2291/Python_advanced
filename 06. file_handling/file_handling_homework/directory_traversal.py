import os

directory = input()
extensions = {}
report = []

for directory_files in os.walk(directory):
    for file_name in directory_files[2]:
        file_path = os.path.join(directory, file_name)

        if '.' in file_path:
            current_extension = file_name.split(".")[-1]

            if current_extension in extensions:
                extensions[current_extension].append(file_name)
            else:
                extensions[current_extension] = [file_name]

extensions = sorted(extensions.items())

for extension, files in extensions:
    report.append(f".{extension}\n")

    for file in sorted(files):
        report.append(f"- - - {file}\n")

with open('report.txt', 'a') as output_file:
    output_file.write("".join(report))
