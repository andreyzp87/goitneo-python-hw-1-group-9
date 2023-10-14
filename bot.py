def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    if len(args) < 2:
        return "Name or phone not present, please try again."
    if len(args) > 2:
        return "Too many parameters, please try again."
    
    name, phone = args
    
    if name in contacts:
        return f"Contact \"{name}\" is already present, use \"change\" command to overwrite the phone."

    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    if len(args) < 2:
        return "Name or phone not present, please try again."
    if len(args) > 2:
        return "Too many parameters, please try again."

    name, phone = args

    if name not in contacts:
        return f"Contact \"{name}\" is not found, use \"add\" command to add it."

    contacts[name] = phone
    return "Contact updated."

def show_phone(args, contacts):
    if len(args) < 1:
        return "No name entered, please try again."
    if len(args) > 1:
        return "Too many parameters, please try again."
    
    name = args[0]
    
    if name not in contacts:
        return f"Contact \"{name}\" is not found."

    return contacts[name]

def show_all(contacts):
    if len(contacts) == 0:
        return "Contacts list is empty."
    
    rows = []
    
    for item in contacts.items():
        name, phone = item
        rows.append(f"{name}: {phone}")
    
    return '\n'.join(rows)

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()