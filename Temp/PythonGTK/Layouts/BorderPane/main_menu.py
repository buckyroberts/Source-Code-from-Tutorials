from gi.repository import Gtk

# UI elements
menu_bar = Gtk.MenuBar()


def create_main_menu(area):

    # File menu
    file_menu = Gtk.Menu()
    menu_item_file = Gtk.MenuItem("File")
    menu_item_file.set_submenu(file_menu)

    # Menu item
    menu_item_exit = Gtk.MenuItem("Quit Now!")
    menu_item_exit.connect("activate", Gtk.main_quit)
    file_menu.append(menu_item_exit)

    # Add file menu to menu bar
    menu_bar.append(menu_item_file)
    area.pack_start(menu_bar, False, False, 0)
