from gi.repository import Gtk


class MenuWindow(Gtk.Window):


    def __init__(self):
        Gtk.Window.__init__(self, title="")
        
        self.set_border_width(10)
        self.set_default_size(500, 400)


        header_bar = Gtk.HeaderBar()
        header_bar.set_show_close_button(True)
        header_bar.props.title = "Rippin Music Player"
        self.set_titlebar(header_bar)
        box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)


        main_menu_bar = Gtk.MenuBar()
        box.add(main_menu_bar)


        # Drop down menu
        file_menu = Gtk.Menu()
        file_menu_dropdown = Gtk.MenuItem("File")


        file_new = Gtk.MenuItem("New")
        file_open = Gtk.MenuItem("Open")
        file_exit = Gtk.MenuItem("Exit")


        file_menu_dropdown.set_submenu(file_menu)


        file_menu.append(file_new)
        file_menu.append(file_open)
        file_menu.append(Gtk.SeparatorMenuItem())
        file_menu.append(file_exit)
        main_menu_bar.append(file_menu_dropdown)


        header_bar.pack_start(box)        


window = MenuWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
