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


def good_bye_command(*args):
    return "Good bye!"


def close_command(*args):
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
    help_command: "help",
    hello_command: "hello",
    add_command: "add",
    exit_command: "exit",
    good_bye_command: "good bye",
    close_command: "close",
    show_all_command: "show all",
    change_command: "change",
    phone_command: "phone"
}


def command_handler(text):
    for command, kword in COMMANDS.items():
        if text.startswith(kword):
            return command, text.replace(kword, "").strip()
    return unknown_command, None


def main():
    print(hello_command())
    while True:
        user_input = input(">>>").lower()
        command, data = command_handler(user_input)
        print(command(data))
        if command in [exit_command, good_bye_command, close_command]:
            break


if __name__ == "__main__":
    main()