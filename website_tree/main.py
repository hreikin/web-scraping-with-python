import simple_menu
from create_tree import run_create_tree
from website_tree.spiders.get_urls import run_spider

app_name = "Tree View"
options = {
    'view': {
        'title':"Run Spider To Generate Links",
        'func': run_spider
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

simple_menu.main_menu(options, app_name)