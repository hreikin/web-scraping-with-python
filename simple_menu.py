def ask_question(question="Do you want to do this action again (yes/no) ? "):
    CONFIRM = "Are you sure you want to do this (yes/no) ? "
    ask = question or CONFIRM
    val = input(ask).lower()
    if val.lower() in "yes":
        return True
    if val.lower() in "no":
        print("OK, cancelling.")
        return False
    # Invalid input response.
    invalid_input()
    return ask_question(question)

def retry_question():
    ask_to_retry = ask_question()
    return ask_to_retry

def print_options(options):
    """Prints something like this for a dict of options:

    e.g. from complex options:

        1. Create a note.
        2. Edit a note.
        3. Delete a note.
        4. List all notes.
        5. Exit/Quit

    example:

        >>> print_options({ 'key': {'title': 'apples', 'other': {'title': 'egg'} }})
        1. apples
        2. egg


    """
    for index, (key, sub_dict) in enumerate(options.items()):
        row = f"{index+1}. {sub_dict['title']}"
        print(row)

def main_menu(options, app_name):
    running = True
    while running:

        print(f"\nWelcome to the {app_name} app.")
        print_options(options)

        q = "Type in a number to make a selection: "
        int_current_selection = ask_number(q)

        choices = tuple(options.values())
        # Takes the users input and runs the appropriate function. If the input is invalid it asks
        # the user to try again.
        try:
            selection = choices[int_current_selection-1]
        except IndexError:
            selection = {
                'title': "Option does not exist.",
                'func': invalid_input,
            }

        print(selection['title'])
        #run our found function
        func = selection['func']
        running = func()
        if running is None:
            running = True

def ask_number(q=None):
    default = "Type in a number to make a selection: "
    try:
        val = input(q or default)
        int_val = int(val)
    except ValueError as e:
        invalid_input()
        return ask_number(q)

    return int_val

def invalid_input():
    default = "Invalid input, please try again."
    print(default)

def close_statement():
    print("Ok, exiting program now.")
    return False
