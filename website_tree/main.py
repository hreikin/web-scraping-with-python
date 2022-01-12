import simple_menu
from create_tree import run_create_tree

options = {
    'view': {
        'title':"Run Spider To Generate Links",
        # 'func': 
    },
    'search': {
        'title':"Create Tree View",
        'func': run_create_tree
    },
    'exit': {
        'title':"Exit the program.",
        'func': simple_menu.close_statement
    },

}

simple_menu.main_menu(options)