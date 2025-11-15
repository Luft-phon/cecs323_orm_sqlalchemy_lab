from menu import Menu
from option import Option


# The main options for operating on Departments and Courses.
menu_main = Menu('main', 'Please select one of the following options:', [
    Option("Add", "add_objects(sess)"),
    Option("List", "list_objects(sess)"),
    Option("Delete", "delete_menu(sess)"),
    Option("Update", "update(sess)"),
    Option("Exit this application", "pass")
])

add_menu = Menu('add', 'Please indicate what you want to add:', [
    Option("Part", "functions.add_part(sess)"),
    Option("Assembly", "functions.add_assembly(sess)"),
    Option("Usage", "functions.add_usage(sess)"),
    Option("Piece Parts", "functions.add_piece_parts(sess)"),
    Option("Vendors", "functions.add_vendors(sess)"),
    Option("Exit", "pass")
])

delete_menu = Menu('delete', 'Please indicate what you want to delete from:', [
    Option("Part", "functions.delete_part(sess)"),
    Option("Assembly", "functions.delete_assembly(sess)"),
    Option("Usage", "functions.delete_usage(sess)"),
    Option("Piece Parts", "functions.delete_piece_parts(sess)"),
    Option("Vendors", "functions.delete_vendors(sess)"),
    Option("Exit", "pass")
])

list_menu = Menu('list', 'Please indicate what you want to list:', [
    Option("Part", "functions.list_part(sess)"),
    Option("Assembly", "functions.list_assembly(sess)"),
    Option("Usage", "functions.list_usage(sess)"),
    Option("Piece Parts", "functions.list_piece_parts(sess)"),
    Option("Vendors", "functions.list_vendors(sess)"),
    Option("Exit", "pass")
])

debug_select = Menu('debug select', 'Please select a debug level:', [
    Option("Informational", "logging.INFO"),
    Option("Debug", "logging.DEBUG"),
    Option("Error", "logging.ERROR")
])
