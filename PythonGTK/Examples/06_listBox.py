from gi.repository import Gtk


# ListBox is just a vertical container that you can sort, navigate with the keyboard, etc...
class ListBoxWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Cheeseburger Machine")
        self.set_border_width(10)
        listbox = Gtk.ListBox()
        listbox.set_selection_mode(Gtk.SelectionMode.NONE)
        self.add(listbox)

        # Inside your ListBox are ListBoxRows (widgets go inside them)
        row_1 = Gtk.ListBoxRow()
        box_1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=100)
        row_1.add(box_1)
        label = Gtk.Label("Check if you love cheeseburgers:")
        check = Gtk.CheckButton()
        box_1.pack_start(label, True, True, 0)
        box_1.pack_start(check, True, True, 0)
        listbox.add(row_1)

        # Toggle switch
        row_2 = Gtk.ListBoxRow()
        box_2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=100)
        row_2.add(box_2)
        label = Gtk.Label("Burger making machine:")
        switch = Gtk.Switch()
        switch.props.valign = Gtk.Align.CENTER
        box_2.pack_start(label, True, True, 0)
        box_2.pack_start(switch, True, True, 0)
        listbox.add(row_2)


win = ListBoxWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
