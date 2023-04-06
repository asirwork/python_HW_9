CONTACTS = {}


def input_error(func):

    def inner(*args):
        try:
            return func(*args)
        except IndexError:
            return "Give me name and phone please"
        except KeyError:
            return "Name not found in contacts"

    return inner


def help_command(*args):
    return "For adding number type add"


def hello_command(*args):
    return "How can I help you?"


def exit_command(*args):
    return "Good bye!"


def unknown_command(*args):
    return "Unknown command, try again."


def show_all_command(*args):
    if not CONTACTS:
        return "No contacts found"
    else:
        result = ""
        for name, numbers in CONTACTS.items():
            result += f"{name}: {''.join(numbers)}\n"
        return result.strip()


@input_error
def change_command(*args):
    params = args[0].split()
    name = params[0]
    new_phone_numbers = ' '.join(params[1:])
    if not new_phone_numbers:
        raise IndexError()
    if name in CONTACTS:
        CONTACTS[name] = new_phone_numbers
        return f"Changed {name} phone number to {new_phone_numbers}"
    else:
        return f"Contact {name} not found"


@input_error
def phone_command(*args):
    params = args[0].split()
    name = params[0]
    if name in CONTACTS:
        return f"{name} has phone number {CONTACTS[name]}"
    else:
        raise KeyError()


@input_error
def add_command(*args):
    params = args[0].split()
    name = params[0]
    phone_numbers = ' '.join(params[1:])
    if not phone_numbers:
        raise IndexError()
    CONTACTS[name] = phone_numbers
    return f"Added {name}, number {phone_numbers}"


COMMANDS = {
    "help": help_command,
    "hello": hello_command,
    "add": add_command,
    "exit": exit_command,
    "good bye": exit_command,
    "close": exit_command,
    "show all": show_all_command,
    "change": change_command,
    "phone": phone_command
}


def command_handler(text):
    for kword, command in COMMANDS.items():
        if text.startswith(kword):
            return command, text.replace(kword, "").strip()
    return unknown_command, None


def main():
    print(hello_command())
    while True:
        user_input = input(">>>").lower()
        command, data = command_handler(user_input)
        print(command(data))
        if command == exit_command:
            break


if __name__ == "__main__":
    main()