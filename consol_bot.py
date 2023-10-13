def hello(*args, contacts):
    return "How can I help you?"

def add(*args, contacts):
    username = args[0]
    phone = args[1]
    contacts[username] = phone
    return f"Added {username} with phone number {phone}"

def change(*args, contacts):
    username = args[0]
    phone = args[1]
    if username in contacts:
        contacts[username] = phone
        return f"Changed {username}'s phone number to {phone}"
    return f"{username} not found"

def phone(*args, contacts):
    username = args[0]
    if username in contacts:
        return contacts[username]
    return f"{username} not found"

def all_contacts(*args, contacts):
    if not contacts:
        return "No contacts saved"
    return "\n".join([f"{username}: {number}" for username, number in contacts.items()])

def exit_bot(*args, contacts):
    return "Good bye!"

def unknown_command(*args, contacts):
    return "Unknown command. Try again"

COMMANDS = {
    hello: "hello",
    add: "add",
    change: "change",
    phone: "phone",
    all_contacts: "all",
    exit_bot: ("exit", "close")
}

def pars_command(line: str) -> tuple[callable, list]:
    for cmd, kwords in COMMANDS.items():
        if line.lower().startswith(kwords):
            return cmd, line.split(" ")[1:]
    return unknown_command, []

def main():
    contacts = {}
    while True:
        user_input = input("Enter command: ").strip()

        command, data = pars_command(user_input)
        print(command(*data, contacts=contacts))
    
        if command == exit_bot:
            break

if __name__ == "__main__":
    main()