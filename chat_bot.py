def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    name, phone = args
    if name not in contacts:
        return 'This contact does not exist'
    else:
        contacts[name] = phone
        return 'Contact changed'


def get_contact(args, contacts):
    name = args[0]
    if name not in contacts:
        return 'This contact does not exist'
    else:
        return f'{name} {contacts[name]}'


def show_all(contacts):
    for user in contacts:
        print(user, contacts[user])


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
        elif command == "all":
            show_all(contacts)
        elif command == "phone":
            print(get_contact(args, contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
