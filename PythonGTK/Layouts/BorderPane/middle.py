from gi.repository import Gtk


# UI elements
button = Gtk.Button()


def create_middle(area):
    button.set_label("Middle Area")
    area.pack_start(button, True, True, 0)
