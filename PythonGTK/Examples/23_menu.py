from gi.repository import Gtk


# gsettings set com.canonical.Unity always-show-menus true
class MenuExampleWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="")
        self.set_default_size(400, 300)

        # Layout
        layout = Gtk.Box()
        self.add(layout)

        # Main container that we will stick inside our layout
        main_menu_bar = Gtk.MenuBar()

        # Drop down menu
        file_menu = Gtk.Menu()
        file_menu_dropdown = Gtk.MenuItem("File")

        # File menu items
        file_new = Gtk.MenuItem("New")
        file_open = Gtk.MenuItem("Open")
        file_exit = Gtk.MenuItem("Exit")

        # File button has dropdown
        file_menu_dropdown.set_submenu(file_menu)

        # Add menu items
        file_menu.append(file_new)
        file_menu.append(file_open)
        file_menu.append(Gtk.SeparatorMenuItem())
        file_menu.append(file_exit)
    
        # Add to main menu bar
        main_menu_bar.append(file_menu_dropdown)

        layout.pack_start(main_menu_bar, True, True, 0)


window = MenuExampleWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
