def people():
    people = {}
    add_person_msg = "Add person to list? (Y/N): "
    first_name_msg = "First name: "
    last_name_msg = "Last name: "

    while input(add_person_msg).lower() == 'y':     #.lower()
        people[input(first_name_msg)] = input(last_name_msg)

    return people

print(people())