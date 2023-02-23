from os import remove


command = input()

while command != "End":
    splited_command = command.split("-")

    current_command = splited_command[0]
    file_name = splited_command[1]

    if current_command == "Create":
        file_to_create = open(f'./{file_name}', 'w')
        file_to_create.close()

    elif current_command == "Add":
        content = splited_command[2]

        with open(f'./{file_name}', 'a') as file_to_add:
            file_to_add.write(f"{content}\n")

    elif current_command == "Replace":
        old_string = splited_command[2]
        new_string = splited_command[3]

        try:
            with open(f'./{file_name}', 'r') as file:
                new_text = file.read().replace(old_string, new_string)

            with open(f'./{file_name}', 'w') as file:
                file.write(new_text)

        except FileNotFoundError:
            print("An error occurred")

    elif current_command == "Delete":

        try:
            remove(f'./{file_name}')

        except FileNotFoundError:
            print("An error occurred")

    command = input()
