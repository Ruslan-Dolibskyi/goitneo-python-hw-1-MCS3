def hello():
    return "How can I help you?"

def add(username, phone, contacts):
    contacts[username] = phone
    return f"Added {username} with phone number {phone}"

def change(username, phone, contacts):
    if username in contacts:
        contacts[username] = phone
        return f"Changed {username}'s phone number to {phone}"
    return f"{username} not found"

def phone(username, contacts):
    if username in contacts:
        return contacts[username]
    return f"{username} not found"

def all_contacts(contacts):
    if not contacts:
        return "No contacts saved"
    return "\n".join([f"{username}: {number}" for username, number in contacts.items()])

def exit_bot():
    return "Good bye!"

def main():
    contacts = {}
    while True:
        command = input("Enter command: ").strip().lower()
        
        if command == "hello":
            print(hello())
            
        elif command.startswith("add "):
            _, username, phone = command.split()
            print(add(username, phone, contacts))
            
        elif command.startswith("change "):
            _, username, phone = command.split()
            print(change(username, phone, contacts))
            
        elif command.startswith("phone "):
            _, username = command.split()
            print(phone(username, contacts))
            
        elif command == "all":
            print(all_contacts(contacts))
            
        elif command in ["close", "exit"]:
            print(exit_bot())
            break

if __name__ == "__main__":
    main()
