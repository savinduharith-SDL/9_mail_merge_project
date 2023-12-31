with open("./Input/Names/invited_names.txt") as invitaion_name_file:
    initial_letter_template = ""
    with open("./Input/Letters/starting_letter.txt") as letter_template:
        initial_letter_template = letter_template.read()
    name_list = invitaion_name_file.readlines()
    for name in name_list:
        stripped_name = name.strip("\n")
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}", mode="w") as new_letter:
            new_letter.write(initial_letter_template.replace("[name]", stripped_name))